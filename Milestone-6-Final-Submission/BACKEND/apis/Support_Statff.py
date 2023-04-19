from flask_restful import Resource
from flask import make_response, jsonify,  Blueprint
from datetime import datetime                   
import pytz

from Models.ticket import Ticket, Category
from Models.user import User, UserType
from db import db

class ResolveTicket(Resource) :

    def put(self, user_id, ticket_id, solution) :

        user = User.get_user_by_id(user_id)

        if user.usertype != UserType.SUPPORT_STAFF :

            response = {
                'message' : 'Only support staff can resolve a Ticket'
            }
            return make_response(jsonify(response), 400)


        ticket = Ticket.get_ticket_by_id(ticket_id)

        if ticket :

            # try :

            ticket.solution = solution
            ticket.solved_at = datetime.now(pytz.timezone('Asia/Kolkata')) 
            ticket.is_resolved = True
            user.solved_ticket.append(ticket)
            
            db.session.commit()
            
            msg = {
                "Ticket_id": ticket.ticket_id,
                    "status": "Query Resolved Successfully!"
            }

            return make_response(jsonify(msg), 200) 
            
            # except :
                
            #     msg = {
            #         "status": "Internal Server Error"
            #         }

            #     return make_response(jsonify(msg), 500)
            

        msg = {
            "status": "Query with given id doesn't exist!"
        }

        return make_response(jsonify(msg), 404)

class PinTicket(Resource) :

    def put(self, user_id, ticket_id) :

        user = User.get_user_by_id(user_id)

        if user.usertype != UserType.SUPPORT_STAFF :

            response = {
                'message' : 'Only support staff can resolve a Ticket'
            }
            return make_response(jsonify(response), 400)

        ticket = Ticket.get_ticket_by_id(ticket_id)

        if ticket :

            try :

                ticket.pin = True
                db.session.commit()
            
                msg = {
                    "Ticket_id": ticket.ticket_id,
                    "status": "Query Pinned successfully!"
                }

                return make_response(jsonify(msg), 200)

            except :

                msg = {
                    "status": "Internal Server Error"
                }

                return make_response(jsonify(msg), 500)
        
        msg = {
               "status": "Query with given id doesn't exist!"
            }

        return make_response(jsonify(msg), 404)

class ReportTicket(Resource) :

    def put(self, user_id, ticket_id) :

        user = User.get_user_by_id(user_id)

        if user.usertype != UserType.SUPPORT_STAFF :

            response = {
                'message' : 'Only support staff can resolve a Ticket'
            }
            return make_response(jsonify(response), 400)
        
        ticket =Ticket.get_ticket_by_id(ticket_id)

        if ticket :

            try :

                ticket.report = True

                response = {
                    "Ticket_id": ticket.ticket_id,
                    "Report": ticket.report
                }

                return make_response(jsonify(response), 200)
            
            except :
                
                response = {
                    "status" : "Internal Server Error"
                }

                return make_response(jsonify(response), 500)
        
        response = {
            "status" : "ticket doesn't exist"
        }

        return make_response(jsonify(response), 404)
