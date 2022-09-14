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


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    username = factory.Faker("name")
    email = factory.Faker("email")
    password = "ivan"


class CategoryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Category

    name = "test_category"
    slug = factory.Faker("slug")


class AdFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Ad

    author = factory.SubFactory(UserFactory)
    name = "test"
    description="test_description"
    price = 15
    is_published = False
    category = factory.SubFactory(CategoryFactory)