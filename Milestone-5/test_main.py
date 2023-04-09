
from main import api
import pytest

## Testing Dashboard API

def test_dashboard_tickets():
    API = api.app.test_client()
    dash = API.get('/dashboard/tickets/Python')

    #assert dash.json == { 'message' : "Internal Server Error" }
    #assert dash.status == "500 INTERNAL SERVER ERROR"

    #dash = API.get('/dashboard/tickets/English')
    #assert dash.json == { 'message' : "Tickets do not exist for the given category" }
    #assert dash.status == "404 NOT FOUND"

    assert dash.json == [{'Ticket_id': 'Python1', 'Created_by': 1, 'Solved_by': 2, 'Category': 'Python', 'Query': 'There is an error in the GA 4 Q7.. Could you please look into it?', 'Solution': 'Dear Student, the quetsion has been updated. Please check.', 'Created_at': '03/23/2023 @ 4:31am', 'Solved_at': '03/23/2023 @ 10:11am', 'IsResolved': 'True', 'AddFAQ': 'True', 'Pin': 'False', 'Report': 'False', 'Likes': 3}]
    assert dash.status == "200 OK"

def test_faq_select():
    API = api.app.test_client()
    query = API.put('/admin/add_ticket_to_faq', data={"Ticket_id": "Python1"})

    #query = API.put('/admin/add_ticket_to_faq', data={"Ticket_id": "Python9"})
    #assert query.status == "404 NOT FOUND"
    #assert query.json == { 'message' : "Query with given id doesn't exist" }

    assert query.status == "200 OK"
    assert query.json == {'Ticket_id': 'Python1', 'status': 'Query AddFAQ status updated!'}
    
def test_delete_ticket():
    API = api.app.test_client()
    query = API.delete('/admin/delete_ticket', data={"Ticket_id": "English7"})

    #query = API.delete('/admin/delete_ticket', data={"Ticket_id": "Python9"})
    #assert query.status == "404 NOT FOUND"
    #assert query.json == { 'message' : "Query with given id doesn't exist" }

    #assert query.status == "405 METHOD NOT ALLOWED"
    #assert query.json == { 'message' : "Operation not allowed as Query hasn't been reported yet." }

    assert query.status == "200 OK"
    assert query.json == {'Ticket_id': 'English7', 'status': 'Query Deleted Successfully!'}

def test_add_faq():
    API = api.app.test_client()
    query = API.post('/FAQ/add_ticket', data={"Ticket_id": "Python1", "Query": 'There is an error in the GA 4 Q7.. Could you please look into it?', 'Solution': 'Dear Student, the quetsion has been updated. Please check.', "Category": "Python"})

    #query = API.post('/FAQ/add_ticket', data={"Ticket_id": "Python1", "Query": 'There is an error in the GA 4 Q7.. Could you please look into it?', 'Solution': 'Dear Student, the quetsion has been updated. Please check.', "Category": "Python"})
    #assert query.status == "409 CONFLICT"
    #assert query.json == { 'message' : "Query already exists in FAQs!" }

    assert query.status == "200 OK"
    assert query.json == {'Ticket_Id': "Python1", 'status': "FAQ doc updated Successfully!"}
    
def test_user():
    API = api.app.test_client()
    dash = API.get('/user')
    assert dash.json == [{"UserId": 1, "UserName": "Joey", "UserType": "Student", "Password": "2pizzas@joeyspecial"}, {"UserId": 2, "UserName": "Ross", "UserType": "Support Staff", "Password": "wewereonabreak"}, {"UserId": 3, "UserName": "Pheobe", "UserType": "Admin", "Password": "SmellyCat"}, {"UserId": 4, "UserName": "Monica", "UserType": "Support Staff", "Password": "chocolate"}]

