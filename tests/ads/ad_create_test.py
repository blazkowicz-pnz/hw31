import pytest

@pytest.mark.django_db
def test_ad_create(client, user, category):
    data = { "author_id": user.id,
            "category_id": category.pk,
            "name": "Котики на продаже1",
            "price": 4,
            "description": "Продам Котиков1",
            "is_published": False,
            }

    r = client.post("/ad/create/", data, content_type="application/json")
    r.data["author_id"] = 4
    r.data["category_id"] = 4

    assert r.status_code == 201
    assert r.data == {
            "name": "Котики на продаже1",
            "author_id": 4,
            "price": 4,
            "description": "Продам Котиков1",
            "is_published": False,
            "category_id": 4,

    }