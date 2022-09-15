# import factory
# from ads.models import Ad, User, Category
#
#
# class CategoryFactory(factory.django.DjangoModelFactory):
#     class Meta:
#         model = Category
#
#     slug = factory.Faker("goods")
#
#
# class UserFactory(factory.django.DjangoModelFactory):
#     class Meta:
#         model = User
#
#     username = factory.Faker("name")
#     email = factory.Faker("name")
#
#
# class AdFactory(factory.django.DjangoModelFactory):
#     class Meta:
#         model = Ad
#
#     category = factory.SubFactory(CategoryFactory)
#     author = factory.SubFactory(UserFactory)
#
#
#
#
#
#
#
#
import factory.django
from ads.models import Ad, User, Category


class CategoryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Category

    slug = factory.Faker("ean", length=8)


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    username = factory.Faker("name")
    email = factory.Faker("email")


class AdFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Ad

    author = factory.SubFactory(UserFactory)
    category = factory.SubFactory(CategoryFactory)
    price = 100
