# import pytest
#
# from ads.serializers.ad import AdSerializer
#
#
# @pytest.mark.django_db
# def test_ads_detail(client, ad, user_token):
#     resp = client.get(f"/ad/{ad.id}/", content_type="application/json", HTTP_AUTHORIZATION="Bearer "+ user_token)
#     assert resp.status_code == 200
#     # assert resp.data == AdSerializer(ad).data
#
import pytest


# @pytest.mark.django_db
# def test_ad_one(client, ad, my_token):
#     expected_response = {
#             "id": ad.pk,
#             "name": "test",
#             "description": "test_descroption",
#             "is_published": False,
#             "author": ad.user_id,
#             "price": 15,
#             "category": ad.category_id
#
#         }
#     response = client.get(f"/ad/{ad.pk}/", HTTP_AUTHORIZATION="Bearer "+ my_token)
#     assert response.status_code == 200
#     assert response.data == expected_response