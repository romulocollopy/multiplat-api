from http import HTTPStatus


def test_schema_empty_query(client):
    resp = client.post("/graphql/")
    assert resp.status_code == HTTPStatus.BAD_REQUEST


def test_schema(client):
    resp = client.post(
        "/graphql/",
        {
            "query": "query UserProfileQuery {\n  viewer {\n    id\n    name\n    email\n  }\n}\n",
            "variables": {},
        },
        content_type="application/json",
    )

    assert resp.status_code == HTTPStatus.OK
    assert resp.json()["data"]["viewer"]["id"] == "user_123"
