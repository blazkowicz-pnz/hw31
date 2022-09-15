from rest_framework import serializers
from rest_framework.generics import get_object_or_404

from ads.models import Ad, User, Category


class AdSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        required=False,
        queryset=User.objects.all(),
        slug_field="username"
    )

    category = serializers.SlugRelatedField(
        required=False,
        queryset=Category.objects.all(),
        slug_field="name"
    )

    class Meta:
        model = Ad
        fields = "__all__"


class AdDetailSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        required=False,
        read_only=True,
        slug_field="username"
    )

    category = serializers.SlugRelatedField(
        required=False,
        read_only=True,
        slug_field="name"
    )

    class Meta:
        model = Ad
        fields = "__all__"


class AdCreateSerializer(serializers.ModelSerializer):
    author_id = serializers.SlugRelatedField(
        required=False,
        queryset=Ad.objects.all(),
        slug_field="username"
    )

    category_id = serializers.SlugRelatedField(
        required=False,
        queryset=Category.objects.all(),
        slug_field="name"
    )

    def is_valid(self, raise_exception=False):
        self._author_id = self.initial_data.pop("author_id")
        self._category_id = self.initial_data.pop("category_id")
        return super().is_valid(raise_exception=raise_exception)

    def create(self, validated_data):
        ad = Ad.objects.create(
            name=validated_data.get("name"),
            description=validated_data.get("description"),
            is_published=validated_data.get("is_published"),
            price=validated_data.get("price")
        )
        ad.author_id = get_object_or_404(User, pk=self._author_id)
        ad.category_id = get_object_or_404(Category, pk=self._category_id)

        ad.save()
        return ad

    class Meta:
        model = Ad
        fields = ("name", "description", "is_published", "author_id", "category_id", "price")