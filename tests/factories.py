import factory
from ads.models import Ad


class AdFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Ad