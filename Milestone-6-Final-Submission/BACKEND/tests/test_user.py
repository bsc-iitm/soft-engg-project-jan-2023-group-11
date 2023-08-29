from app import app

def test_user_sign_up() :

    response = app.test_client().post('/user/adduser/johndoe/12345/STUDENT')

    print(response)
    assert response.status_code == 201


def test_user_sign_up_dup(client) :

    response = app.test_client().post('/user/adduser/johndoe/12345/STUDENT')

    print(response)
    assert response.status_code == 409
