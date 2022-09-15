import pytest

from ads.serializers.ad import AdSerializer

@pytest.mark.django_db
def test_ad_detail(client, ad, my_token):

    resp = client.get(f"/ad/{ad.id}/", content_type="application/json", HTTP_AUTHORIZATION="Bearer "+ my_token)
    assert resp.status_code == 200
    assert resp.data == AdSerializer(ad).data