from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.auth import authenticate
from django.views.decorators.csrf import csrf_exempt
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
from .models import KeyboardMouseCoordinationResult
from django.db import transaction
from django.utils import timezone


@transaction.atomic
@csrf_exempt
@api_view(['GET', 'POST'])
@permission_classes((AllowAny,))
def results_view(request):
    # print(BallsRedBalls.objects.all().last().json['hello'])
    if request.method == 'GET':
        if not request.user.is_authenticated:
            return Response({'results': 'Unauthorized'}, status=HTTP_200_OK)
    if request.method == 'POST':
        # 'user', 'trial', 'time', 'hit', 'speed', 'radius', 'balls', 'keyboard_step', 'sensitivity', 'created_at'
        trial = str(request.data.get("playedGames")) + "/" + str(request.data.get("countOfGames"))
        time = request.data.get("time")
        hit = request.data.get("mode")
        speed = request.data.get("speed")
        radius = request.data.get("radius")
        balls = request.data.get("ballsCount")
        keyboard_step = request.data.get("keyboardStep")
        sensitivity = request.data.get("sensitivity")
        result = KeyboardMouseCoordinationResult(user=request.user, trial=trial, time=time, hit=hit, speed=speed, radius=radius, balls=balls, keyboard_step=keyboard_step, sensitivity=sensitivity)
        result.save()

    results = KeyboardMouseCoordinationResult.objects.filter(user=request.user)[0:30].values()
    for result in results: result["created_at"] = result["created_at"].astimezone(timezone.get_default_timezone()).strftime('%d/%m/%Y, %H:%M')
    return Response({
        'username': request.user.username,
        'results': list(results)
    }, status=HTTP_200_OK)
