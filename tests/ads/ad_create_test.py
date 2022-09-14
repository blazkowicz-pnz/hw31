# import pytest
#
# @pytest.mark.django_db
# def test_ad_create(client, user, category):
#     resp = client.post("/ad/create/", {
#             "author_id": user.pk,
#             "category_id": category.pk,
#             "name": "Котики на продаже1",
#             "price": 4,
#             "description": "Продам Котиков1",
#             "is_published": False,
#             "image": None
#         }, content_type="application/json")
#
#     assert resp.status_code == 200
#     # assert resp.data == {
#     #         "id": 3,
#     #         "name": "Котики на продаже1",
#     #         "author": user.pk,
#     #         "price": 4,
#     #         "description": "Продам Котиков1",
#     #         "is_published": False,
#     #         "category": category.pk,
#     #         "image": None
#     # }