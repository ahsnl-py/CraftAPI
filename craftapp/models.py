from craftapp import db

class ClientContactDetails(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    fullname = db.Column(db.String(120), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    request_detail = db.Column(db.Text, nullable=True)

    def __repr__(self):
        return '<ClientContactDetails %r>' % self.fullname

    def __init__(self, fullname, email, request_detail):
        self.fullname = fullname 
        self.email = email  
        self.request_detail = request_detail 