# import pytest
#
# @pytest.fixture()
# @pytest.mark.django_db
# def user_token(client, django_user_model):
#     username = "test_user"
#     password = "testpass"
#     email = "test@test.ru"
#     django_user_model.objects.create_user(username=username, password=password, email=email)
#
#     response = client.post("/user/token/", {"username": username, "password": password}, content_type="application/json")
#     return response.data["access"]
import pytest


@pytest.fixture
@pytest.mark.django_db
def my_token(client, django_user_model):
    username = "ivan"
    password = "ivan"
    email = "ivan@ivan.ru"

    django_user_model.objects.create_user(
        username=username, password=password, email=email, role="admin"
    )

    response = client.post("/user/token/", {
        "username": username,
        "password": password
    },
    format="json"
    )
    return response.data["access"]
