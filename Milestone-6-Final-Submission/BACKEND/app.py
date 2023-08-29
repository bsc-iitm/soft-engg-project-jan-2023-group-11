from flask import Flask, Blueprint
from flask_restful import Api
from flask_cors import CORS


from apis.user import UserResource, UserLoginResource
from apis.student import StudentResource, StudentLikeTicket
from apis.Support_Statff import ResolveTicket, ReportTicket, PinTicket
from apis.dashboard import Dashboard, DashboardCategory
from apis.admin import FAQ




app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///./store.sqlite3'
app.config['SQLALCHEMY_ECHO'] = False
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
api = Api(app)
# db = SQLAlchemy(app)
app.test_client()

cors = CORS(app, resource={
    r"/*":{
        "origins":"*"
    }
})



@app.before_first_request
def create_table():
    db.create_all()

api.add_resource(UserResource, '/user/adduser/<string:username>/<string:password>/<string:usertype>')
api.add_resource(UserLoginResource, '/user/login/<string:username>/<string:password>')
api.add_resource(Dashboard, '/dashboard')
api.add_resource(DashboardCategory, '/dashboard/<string:category>')
api.add_resource(StudentResource, '/student/create_ticket/<int:user_id>/<string:title>/<string:category>/<string:query>')
api.add_resource(StudentLikeTicket, '/student/like_ticket/<int:ticket_id>')
api.add_resource(ResolveTicket,'/support_staff/<int:user_id>/resolve/<int:ticket_id>/<string:solution>')
api.add_resource(ReportTicket,'/support_staff/<int:user_id>/report_ticket/<int:ticket_id>')
api.add_resource(PinTicket,'/support_staff/<int:user_id>/pin_ticket/<int:ticket_id>')
api.add_resource(FAQ, '/admin/<int:user_id>/faq/<int:ticket_id>')



if __name__ == '__main__' :

    from db import db

    db.init_app(app)
    app.run(host='127.0.0.1', port=5001,debug=True)
