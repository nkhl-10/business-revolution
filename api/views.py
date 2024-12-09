from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from user.models import register as UserData
from innovator.models import category_innovator as CategoryData
from innovator.models import innovator_uploads as IdeaData
from api.serializers import UserDataSerializers
from api.serializers import IdeaDataSerializers
from api.serializers import CategoryDataSerializers

GET = 'GET'
POST = 'POST'
PUT = 'PUT'
DELETE = 'DELETE'


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
def getSingleUser(request, id):
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


@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def categoryHandle(request, id=None):
    if request.method == GET:
        if id:
            category = CategoryData.objects.get(id=id)
            serializer = CategoryDataSerializers(category)
            return Response(serializer.data)

        else:
            category = CategoryData.objects.all()
            serializer = CategoryDataSerializers(category, many=True)
            return Response(serializer.data)

    elif request.method == POST:
        serializer = CategoryDataSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == PUT:
        if id:
            category = CategoryData.objects.get(id=id)
            serializer = CategoryDataSerializers(category, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)

    elif request.method == DELETE:
        if id:
            category = CategoryData.objects.get(id=id)
            category.delete()
            return Response({"message": "Idea deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
        return Response({"error": "ID is required for deleting"}, status=status.HTTP_400_BAD_REQUEST)
