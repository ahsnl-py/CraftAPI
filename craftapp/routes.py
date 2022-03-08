import pandas as pd
from flask_restful import Resource, Api
from flask import request, jsonify
from flask_cors import CORS, cross_origin

from craftapp.models import ClientContactDetails
from craftapp import server, db

CORS(server)
api = Api(server)

def format_contact_client(client):
    return {
        "fullname": client.fullname,
        "email": client.email,
        "request_detail": client.request_detail
    }

@server.route('/api/contactlist',  methods=['GET', 'POST']) #
@cross_origin()
def create_contact_client():
    print(request.method)
    
    if request.method == "POST":
        print(request.json)
        fullname = request.json['fullname']
        email = request.json['email']
        request_detail = request.json['request_detail']
        new_client = ClientContactDetails(  
                        fullname=fullname
                        , email=email
                        , request_detail=request_detail
                    )
        db.session.add(new_client)
        db.session.commit()
        return format_contact_client(new_client)

    elif request.method == "GET":
        query = f"""
                    SELECT * FROM client_contact_details
                """
        df_sly = pd.read_sql_query(query, con=db.engine)
        return jsonify(df_sly.to_dict('records'))


# class getTeamInfo(Resource):
#     def get(self):
#         query = f"""
#                     SELECT * from employee
#                 """
#         df_sly = pd.read_sql_query(query, con=db.engine)
#         season_list = list()
#         for i in df_sly['lastname']:
#             season_list.append(i)
#         return jsonify(dict(list(enumerate(season_list))))

# api.add_resource(getTeamInfo, '/')