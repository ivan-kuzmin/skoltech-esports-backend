from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.auth import authenticate, logout
from django.views.decorators.csrf import csrf_exempt
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, permission_classes
from rest_framework.status import (
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND,
    HTTP_200_OK
)
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from django.contrib.auth.models import User
from api_v0.serializers import UserSerializer
from django.db import transaction
import json
from django.utils import timezone


# def home_view(request):
#     print(request.user)
    # if request.method == 'POST':
    #     print("TRY LOGIN")
    #     user = authenticate(username=request.POST.get('username'), password=request.POST.get('password'))
    #     if user is not None and user.is_active:
    #         login(request, user)
    #         # if not request.POST.get('remember_me', None):
    #         #     request.session.set_expiry(0)
    #         return JsonResponse({"status": True, "user": str(request.user)})
    # return JsonResponse({"user": str(request.user)})
    # return render(request, 'index.html', {})


@csrf_exempt
@api_view(['GET', 'POST'])
@permission_classes((AllowAny,))
def home_view(request):
    if request.method == 'GET':
        return Response({'username': str(request.user)}, status=HTTP_200_OK)
    elif request.method == 'POST':
        username = request.data.get("username")
        password = request.data.get("password")
        # print(request.data)
        if username is None or password is None:
            return Response({'error': 'Please provide both username and password'}, status=HTTP_400_BAD_REQUEST)
        user = authenticate(username=username, password=password)
        if not user:
            return Response({'error': 'Invalid Credentials'}, status=HTTP_404_NOT_FOUND)
        token, _ = Token.objects.get_or_create(user=user)
        return Response({'token': token.key}, status=HTTP_200_OK)


@csrf_exempt
@api_view(['POST'])
@permission_classes((AllowAny,))
def logout_view(request):
    request.user.auth_token.delete()
    logout(request)
    return Response({'user': str(request.user)}, status=HTTP_200_OK)


# @api_view(['GET', 'POST'])
# def home_view(request):
#     """
#     List all code snippets, or create a new snippet.
#     """
#     if request.method == 'GET':
#         users = User.objects.all()
#         serializer = UserSerializer(users, many=True)
#         return Response(serializer.data)
#
#     elif request.method == 'POST':
#         serializer = UserSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
