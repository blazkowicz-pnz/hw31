from rest_framework import serializers

from ads.models import User, Location, Category, Ad


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = "__all__"


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


class UserListSerializer(serializers.ModelSerializer):
    locations = serializers.SlugRelatedField(

        # queryset=Location.objects.all(),
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

    class Meta:
        model = User
        fields = "__all__"

    def is_valid(self, raise_exception=False):
        self._locations = self.initial_data.pop("location")
        return super().is_valid(raise_exception=raise_exception)

    def create(self, validated_data):
        user = User.objects.create(**validated_data)
        for location in self._locations:
            location_obj, _ = Location.objects.get_or_create(name=location)
            user.locations.add(location_obj)
        user.save()
        return user


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
    id = serializers.IntegerField(required=False)
    author = serializers.SlugRelatedField(
        queryset=User.objects.all(),
        required=False,
        slug_field="username"
    )

    category = serializers.SlugRelatedField(
        queryset=Category.objects.all(),
        required=False,
        slug_field="name"
    )

    class Meta:
        model = Ad
        fields = "__all__"

    def is_valid(self, raise_exception=False):
        self._author = self.initial_data.pop("author")
        self._category = self.initial_data.pop("category")
        return super().is_valid(raise_exception=raise_exception)

    def create(self, validated_data):
        ad = Ad.objects.create(**validated_data)
        for aut in self._author:
            aut_obj, _ = Ad.objects.get_or_create(name=aut)
            ad.author.add(aut_obj)

        for cat in self._category:
            cat_obj, _ = Ad.objects.get_or_create(name=cat)
            ad.category.add(cat_obj)

        ad.save()
        return ad


class AdUpdateSerializer(serializers.ModelSerializer):
    author = serializers.CharField(read_only=True)
    category = serializers.SlugRelatedField(
        queryset=Category.objects.all(),
        required=False,
        slug_field="name"
    )

    class Meta:
        model = Ad
        fields = "__all__"

    def is_valid(self, raise_exception=False):
        if "category" in self.initial_data:
            self._category = self.initial_data.pop("category")
        else:
            self._category = ""
        return super().is_valid(raise_exception=raise_exception)

    def save(self):
        ad = super().save()
        for cat in self._category:
            cat_obj, _ = Ad.objects.get_or_create(name=cat)
            ad.catecory.add(cat_obj)
        return ad

    class AdDeleteSerializer(serializers.ModelSerializer):
        class Meta:
            model = Ad
            fields = "__all__"

    # def is_valid(self, raise_exception=False):
    #
    #     if "locations" in self.initial_data:
    #         self._locations = self.initial_data.pop("locations")
    #     else:
    #         self._locations = []
    #     return super().is_valid(raise_exception=raise_exception)
    #
    # def save(self, **kwargs):
    #     user = super().save(**kwargs)
    #     for locations in self._locations:
    #         obj, _ = Location.objects.get_or_create(name=locations)
    #         user.locations.add(obj)
    #     return user
