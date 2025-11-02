from http import HTTPStatus


def test_home(client):
    resp = client.get("/graphql/")
    assert resp.status_code == HTTPStatus.OK
