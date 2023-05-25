from api.questions_api import api
from http import HTTPStatus
from utils.assertion import Assert

def test_list_users():

    response = api.list_users()

    assert response.status_code == HTTPStatus.OK
    Assert.validate_schema(response.json())
def test_single_user_not_found():

    response = api.single_user_not_found()

    assert response.status_code == HTTPStatus.NOT_FOUND
    Assert.validate_schema(response.json())

def test_single_user():

    response = api.single_user()
    response_body = response.json()

    assert response.status_code == HTTPStatus.OK
    Assert.validate_schema(response_body)
    assert response_body["data"]["first_name"] == "Janet"
    example = {
            "data": {
                "id": 2,
                "email": "janet.weaver@reqres.in",
                "first_name": "Janet",
                "last_name": "Weaver",
                "avatar": "https://reqres.in/img/faces/2-image.jpg"
            },
            "support": {
                "url": "https://reqres.in/#support-heading",
                "text": "To keep ReqRes free, contributions towards server costs are appreciated!"
            }
    }

    assert example == response_body

def test_create():
    name = 'TTTT'
    job = 'jjjj'
    response = api.create(name,job)

    assert response.status_code == HTTPStatus.CREATED
    assert response.json()['name'] == name
    assert response.json()['job'] == job

    assert api.delete_user(response.json()['id']).status_code == HTTPStatus.NO_CONTENT