from http import HTTPStatus


def test_root_deve_retornar_ok_e_ola_mundo(client):

    response = client.get('/')

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {'message': 'Hello!'}


def test_create_user(client):
    response = client.post(
        '/users/',
        json={
            'username': 'Juba',
            'email': 'juba@email.com',
            'password': 'secret',
        },
    )

    assert response.status_code == HTTPStatus.CREATED
    assert response.json() == {
        'username': 'Juba',
        'email': 'juba@email.com',
        'id': 1,
    }
