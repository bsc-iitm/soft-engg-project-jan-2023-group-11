
import json
import pytest
from student import app, db, Ticket

@pytest.fixture
def client():
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    with app.test_client() as client:
        with app.app_context():
            db.create_all()
    yield client
    db.drop_all()

def test_create_ticket(client):
    
    # Test creating a new ticket
    ticket_data = {
         'Ticket_id': 'T001',
         'Created_by': 1,
         'Solved_by': None,
         'Category': 'General',
         'Query': 'This is a test query.',
         'Created_at': '2022-03-23 11:30:00',
         'Solved_at': None,
         'IsResolved': False,
         'AddFAQ': False,
         'Pin': False,
         'Report': False,
         'Likes': 0 }
    response = client.post('/Student/create_ticket/1/General/This is a test query.', json=ticket_data)
    assert response.status_code == 200
    assert Ticket.query.filter_by(ticket_id='T001').first() is not None

    # Test creating a ticket with existing query
    response = client.post('/Student/create_ticket/1/General/This is a test query.', json=ticket_data)
    assert response.status_code == 403

def test_like_ticket(client):
    # Create a ticket
    ticket_data = {
         'Ticket_id': 'T002',
         'Created_by': 1,
         'Solved_by': None,
         'Category': 'General',
         'Query': 'This is a test query.',
         'Created_at': '2022-03-23 11:30:00',
         'Solved_at': None,
         'IsResolved': False,
         'AddFAQ': False,
         'Pin': False,
         'Report': False,
         'Likes': 0  }
    client.post('/Student/create_ticket/1/General/This is a test query.', json=ticket_data)

    # Test liking a ticket
    like_data = {'Likes': 1}
    response = client.put('/Student/like_ticket/T002', json=like_data)
    assert response.status_code == 200
    assert Ticket.query.filter_by(ticket_id='T002').first().likes == 1

    # Test liking a ticket that doesn't exist
    response = client.put('/Student/like_ticket/T003', json=like_data)
    assert response.status_code == 404

    
