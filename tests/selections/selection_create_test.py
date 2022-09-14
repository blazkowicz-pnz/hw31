# import pytest
#
# @pytest.mark.django_db
# def test_selection_create(client, user, ad, user_token):
#     response = client.post("/selection/create/", {
#         "name": "test_selection",
#         "owner": user.pk,
#         "items": [ad.pk]
#     }, content_type="application/json", HTTP_AUTHORIZATION = "Bearer "+ user_token)
#
#     assert response.status_code == 201
#     assert response.data == {
#         "id": 1,
#         "name": "test_selection",
#         "owner": user.pk,
#         "items": [ad.pk]
#     }

import pytest

@pytest.mark.django_db
def test_create_selection(client, my_token):

    expected_response = {
        "id": 2,
        "name": "mans11",
        "owner": 1,
        "items": [
            1
        ]
    }

    data = {
        "name": "mans11",
"owner": 1,
"items":[1]

    }

    response = client.post("/selection/create/", data, content_type="application/json", HTTP_AUTHORIZATION="Bearer "
                                                                                                           + my_token)

    assert response.status_code == 201
    assert response.data == expected_response