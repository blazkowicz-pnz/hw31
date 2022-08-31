from rest_framework import serializers
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