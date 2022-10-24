import requests
from requests import Response
from voluptuous import Schema, PREVENT_EXTRA, Optional
from pytest_voluptuous import S
import schemas.schemas as schema
from utils.base_session import reqres_session


def test_get_single_user():
    response: Response = requests.get("https://reqres.in/api/users/2")

    assert response.status_code == 200
    assert response.json() == S(schema.get_single_user_schema)
    assert response.json()['data']['id'] == 2
    assert response.json()['data']['email'] == 'janet.weaver@reqres.in'
    assert response.json()['data']['first_name'] == 'Janet'
    assert response.json()['data']['last_name'] == 'Weaver'


def test_create_user():
    name = 'Elena'
    job = 'artist'

    create = requests.post(
        url="https://reqres.in/api/users",
        json={"name": name, "job": job}
    )

    assert create.status_code == 201
    assert create.json() == S(schema.create_user_schema)
    assert create.json()["name"] == name
    assert create.json()["job"] == job
    assert isinstance(create.json()["id"], str)
    assert isinstance(create.json()["createdAt"], str)


def test_update_user():
    name = "Elena"
    job = "dancer"

    result: Response = reqres_session().put(
        url="/api/users/2",
        json={"name": name, "job": job}
    )

    print(result.text)

    assert result.status_code == 200
    assert result.json()['name'] == name
    assert result.json()['job'] == job
    assert result.json() == S(schema.update_user_schema)


def test_successful_register_user():
    email = "eve.holt@reqres.in"
    password = "pistol"

    result: Response = reqres_session().post(
        url="/api/register",
        json={
            "email": email,
            "password": password
        }
    )

    print(result.text)

    assert result.status_code == 200
    assert result.json() == S(schema.successful_register_user_schema)
    assert result.json()["id"] == 4
    assert isinstance(result.json()["id"], int)
    assert result.json()["token"] == "QpwL5tke4Pnpja7X4"
    assert isinstance(result.json()["token"], str)


def test_delete_user():
    result: Response = reqres_session().delete(
        url="/api/users/2"
    )
    print(result.text)
    assert result.status_code == 204