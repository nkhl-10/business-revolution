from rest_framework import serializers
from user.models import register as UserData
from innovator.models import innovator_uploads as IdeaData
from innovator.models import category_innovator as CategoryData


class UserDataSerializers(serializers.ModelSerializer):
    class Meta:
        model = UserData
        fields = '__all__'


class IdeaDataSerializers(serializers.ModelSerializer):
    class Meta:
        model = IdeaData
        fields = '__all__'


class CategoryDataSerializers(serializers.ModelSerializer):
    class Meta:
        model = CategoryData
        fields = '__all__'
