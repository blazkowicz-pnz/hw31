import pytest

@pytest.mark.django_db
def test_ad_create(client, user, category):
    data = { "author_id": user.pk,
            "category_id": category.pk,
            "name": "Котики на продаже1",
            "price": 4,
            "description": "Продам Котиков1",
            "is_published": False,
            "image": None
                 }

    r = client.post("/ad/create/", data, content_type="application/json")

    assert r.status_code == 200
    # assert resp.data == {
    #         "id": 1,
    #         "name": "Котики на продаже1",
    #         "author_id": user.pk,
    #         "price": 4,
    #         "description": "Продам Котиков1",
    #         "is_published": False,
    #         "category_id": category.pk,
    #         "image": None
    # }