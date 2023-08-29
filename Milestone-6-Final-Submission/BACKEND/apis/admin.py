from flask_restful import Resource
from flask import make_response, jsonify, Blueprint

from db import db
from Models.ticket import Ticket
from Models.user import User, UserType

class FAQ(Resource) :

    def put(self, user_id,ticket_id) :

        user = User.get_user_by_id(user_id)

        if user.usertype != UserType.ADMIN :

            response = {
                'message' : 'Only Admin can do this operation'
            }

            return make_response(jsonify(response), 400)


        ticket = Ticket.get_ticket_by_id(ticket_id)

        if ticket :

            try :

                ticket.is_faq = True
                db.session.commit()

                response = {
                    "Ticket_id": ticket.ticket_id,
                    "AddFAQ": ticket.is_faq
                }

                return make_response(jsonify(response), 200)
            
            except :

                response = {
                    "status": "Internal Server Error"
                }
                
                return make_response(jsonify(response), 500)
        
        response = {
            "status": "Query with given id doesn't exist!"
        }

        return make_response(jsonify(response), 404)


    def delete(self, user_id, ticket_id) :

        user = User.get_user_by_id(user_id)

        if user.usertype != UserType.ADMIN :

            response = {
                'message' : 'Only Admin can do this operation'
            }
            
            return make_response(jsonify(response), 400)

        ticket = Ticket.get_ticket_by_id(ticket_id)

        if ticket :

            try :
                _id = ticket.ticket_id
                ticket.delete()
                db.session.commit()

                response = {
                    "Ticket_id": _id,
                    "status": "Query Deleted successfully!"
                }

                return make_response(jsonify(response), 200)
            
            except :

                response = {
                    "status": "Internal Server Error"
                }
                
                return make_response((jsonify(response)), 500)
        
        response = {
            "status": "Query with given id doesn't exist!"
        }

        return make_response(jsonify(response), 404)
