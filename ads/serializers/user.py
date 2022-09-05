from rest_framework import serializers
from ads.models import User, Location


class UserListSerializer(serializers.ModelSerializer):
    locations = serializers.SlugRelatedField(
        read_only=True,
        many=True,
        slug_field="name",
    )

    class Meta:
        model = User
        exclude = ["password"]


class UserDetailSerializer(serializers.ModelSerializer):
    locations = serializers.SlugRelatedField(
        read_only=True,
        many=True,
        slug_field="name",

    )

    class Meta:
        model = User
        exclude = ["password"]


class UserCreateSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)
    locations = serializers.SlugRelatedField(
        required=False,
        many=True,
        queryset=Location.objects.all(),
        slug_field="name"
    )

    def is_valid(self, raise_exception=False):
        self._locations = self.initial_data.pop("locations")
        return super().is_valid(raise_exception=raise_exception)

    def create(self, validated_data):
        user = User.objects.create(**validated_data)
        user.set_password(validated_data["password"])
        user.save()
        for locations in self._locations:
            location_obj, _ = Location.objects.get_or_create(name=locations)
            user.locations.add(location_obj)
        return user

    class Meta:
        model = User
        fields = "__all__"


class UserUpdateSerializer(serializers.ModelSerializer):
    # id = serializers.IntegerField(required=False)
    locations = serializers.SlugRelatedField(
        required=False,
        queryset=User.objects.all(),
        many=True,
        slug_field="name"
    )

    class Meta:
        model = User
        fields = "__all__"

    def is_valid(self, raise_exception=False):

        if "locations" in self.initial_data:
            self._locations = self.initial_data.pop("locations")
        else:
            self._locations = []
        return super().is_valid(raise_exception=raise_exception)

    def save(self, **kwargs):
        user = super().save(**kwargs)
        for locations in self._locations:
            obj, _ = Location.objects.get_or_create(name=locations)
            user.locations.add(obj)
        return user


class UserDeleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"
