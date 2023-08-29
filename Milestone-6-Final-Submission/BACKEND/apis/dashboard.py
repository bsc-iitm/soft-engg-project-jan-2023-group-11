from flask_restful import Resource
from flask import make_response,jsonify, Blueprint
from Models.ticket import Ticket
from Models.user import User

class Dashboard(Resource) :

    def get(self) :

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
                'title' : ticket.title,
                'created_at' : ticket.created_at,
                'solved_at' : ticket.solved_at,
                'id' : ticket.ticket_id
            }
            for ticket in tickets
        ]

        response = {
            "queries" : json_ticket[::-1]
        }

        return make_response(jsonify(response),200)

class DashboardCategory(Resource) :

    def get(self,category) :

        print(category)

        try :

            tickets = Ticket.get_ticket_by_category(category=category)

            json_ticket = [
                 {
                'id' : ticket.ticket_id,
                'query' : ticket._query,
                'solution' : ticket.solution if ticket.solution else None,
                'created_by' : [user.username for user in ticket.created_user],
                'solved_by' :  [user.username for user in ticket.solved_user] if ticket.solved_user else None            
            }
                for ticket in tickets
            ]

            # print(json_ticket)

            return make_response(jsonify(json_ticket),200)
        
        except :

            return make_response(jsonify({
                "message" : "Something went wrong. Please try again."
            }), 500)
        
        