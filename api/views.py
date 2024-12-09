from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from user.models import register as UserData
from innovator.models import innovator_uploads as IdeaData
from api.serializers import UserDataSerializers
from api.serializers import IdeaDataSerializers


@api_view(['GET'])
def getData(request):
    return Response({'value': 'you not have endpoint'})


# User CRUD Views
@api_view(['GET'])
def getAllUsers(request):
    users = UserData.objects.all()
    serializer = UserDataSerializers(users, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def getSingleUser(request,id):
    try:
        user = UserData.objects.get(id=id)
        serializer = UserDataSerializers(user)
        return Response(serializer.data)
    except UserData.DoesNotExist:
        return Response({"error": "User not found"}, status=status.HTTP_404_NOT_FOUND)


@api_view(['POST'])
def addUser(request):
    serializer = UserDataSerializers(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT'])
def updateUser(request, id):
    try:
        user = UserData.objects.get(id=id)
    except UserData.DoesNotExist:
        return Response({"error": "User not found"}, status=status.HTTP_404_NOT_FOUND)
    serializer = UserDataSerializers(user, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def deleteUser(request, id):
    try:
        user = UserData.objects.get(id=id)
        user.delete()
        return Response({"message": "User deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
    except UserData.DoesNotExist:
        return Response({"error": "Idea not found"}, status=status.HTTP_404_NOT_FOUND)


# Idea CRUD Views
@api_view(['GET'])
def getAllIdeas(request):
    ideas = IdeaData.objects.all()
    serializer = IdeaDataSerializers(ideas, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def getSingleIdea(request, id):
    try:
        idea = IdeaData.objects.get(id=id)
        serializer = IdeaDataSerializers(idea)
        return Response(serializer.data)
    except IdeaData.DoesNotExist:
        return Response({"error": "Idea not found"}, status=status.HTTP_404_NOT_FOUND)


@api_view(['POST'])
def addIdea(request):
    serializer = IdeaDataSerializers(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT'])
def updateIdea(request, id):
    try:
        idea = IdeaData.objects.get(id=id)
    except IdeaData.DoesNotExist:
        return Response({"error": "Idea not found"}, status=status.HTTP_404_NOT_FOUND)
    serializer = IdeaDataSerializers(idea, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def deleteIdea(request, id):
    try:
        idea = IdeaData.objects.get(id=id)
        idea.delete()
        return Response({"message": "Idea deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
    except IdeaData.DoesNotExist:
        return Response({"error": "Idea not found"}, status=status.HTTP_404_NOT_FOUND)
