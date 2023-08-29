from flask_restful import Resource
from flask import make_response, jsonify, Blueprint

from Models.user import User, UserType
from Models.ticket import Ticket
from db import db

class StudentResource(Resource) :

    def post(self, user_id, title, category, query) :
        print(category)
        user = User.get_user_by_id(user_id)
        
        if user.usertype != UserType.STUDENT :

            return make_response(jsonify({
                'message' : 'Only a Student can create a ticket' 
            }))

        
        try :

            ticket = Ticket(title, query, category)
            ticket.create_query()
            user.created_tickets.append(ticket)
            db.session.commit()

            tickets = Ticket.get_all_ticket()

            json_ticket = [
                {
                    'query' : ticket._query,
                    'solution' : ticket.solution if ticket.solution else None,
                    'created_by' : [user.username for user in ticket.created_user][0],
                    'solved_by' :  [user.username for user in ticket.solved_user][0] if ticket.solved_user else None,            
                    'status' : "Resolved" if ticket.is_resolved else "Not Resolved",
                    'likes' : ticket.likes,
                    'category' :ticket.category,
                    'title' : ticket.title
                }
                for ticket in tickets
            ]

            msg = {
                'message' : 'Ticket created Successfully',
                'queries' : json_ticket[::-1]
            }

            return make_response(jsonify(msg), 201)
        
        except  :
        

            msg = {
                'message' : 'Internal Server Error'
            }

            return make_response(jsonify(msg), 500)

class StudentLikeTicket(Resource) :

    def put(self, ticket_id) :

        ticket = Ticket.get_ticket_by_id(ticket_id)

        if ticket :
            print(ticket.likes)
            try :
                
                if ticket.likes == 0:
                    ticket.likes = 1
                else :
                    ticket.likes = ticket.likes + 1

                db.session.commit()
                response = {
                    "Ticket_id": ticket.ticket_id,
                    "Likes": ticket.likes
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



    