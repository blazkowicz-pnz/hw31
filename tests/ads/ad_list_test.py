# import pytest
#
# from ads.serializers.ad import AdSerializer
# from tests.factories import AdFactory
#
#
# @pytest.mark.django_db
# def test_ads_test(client):
#     ads_factories = AdFactory.create_batch(5)
#
#     response = client.get("/ad/")
#     assert response.status_code == 200
#     assert response.data == {
#         "count": 5,
#         "next": None,
#         "previous": None,
#         "results": AdSerializer(ads_factories, many=True).data
#     }
# import pytest
#
# from ads.models import Ad
#
# @pytest.mark.django_db
# def test_ad_list(client):
#     ad = Ad.objects.create(
#     name="Лошадь продам",
#     description="Конь на продажу",
#     price=15,
#     image=None,
#     author_id=None,
#     is_published=False,
#     category_id=None
#
#
#     )
#
#     expected_response = {
#         "count": 1,
#         "next": None,
#         "previous": None,
#         "results": [
#             {
#                 "id": ad.pk,
#                 "name": "Лошадь продам",
#                 "author": "ivan",
#                 "price": 15,
#                 "description": "Конь на продажу",
#                 "is_published": False,
#                 "category": None,
#                 "image": None
#             }
#         ]
#     }
#     response = client.get("/ad/")
#     assert response.status_code == 200
#     assert response.data == expected_response
#

