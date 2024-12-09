from rest_framework import serializers
from user import models as UserData
from innovator import models as IdeaData


class UserDataSerializers(serializers.ModelSerializer):
    class Meta:
        model = UserData.register
        fields = '__all__'


class IdeaDataSerializers(serializers.ModelSerializer):
    class Meta:
        model = IdeaData.innovator_uploads
        fields = '__all__'
