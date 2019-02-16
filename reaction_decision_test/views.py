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
from .models import ReactionDecisionTestResult
from django.db import transaction
from django.utils import timezone


@transaction.atomic
@csrf_exempt
@api_view(['GET', 'POST'])
@permission_classes((AllowAny,))
def results_view(request):
    if request.method == 'GET':
        if not request.user.is_authenticated:
            return Response({'results': 'Unauthorized'}, status=HTTP_200_OK)
    if request.method == 'POST':
        # "user", "level", "success", "correct_result", "color", "radius", "x", "y", "width", "height", "time_reaction", "created_at"
        level = request.data.get("level")
        success = request.data.get("success")
        correct_result = request.data.get("correct_result")
        color = request.data.get("color")
        radius = request.data.get("radius")
        x = request.data.get("x")
        y = request.data.get("y")
        width = request.data.get("width")
        height = request.data.get("height")
        time_reaction = request.data.get("time_reaction")
        result = ReactionDecisionTestResult(level=level, success=success, user=request.user, correct_result=correct_result, color=color, time_reaction=time_reaction, x=x, y=y, width=width, height=height, radius=radius)
        result.save()

    first_level = {
        'level': 1,
    }

    # first_result = ReactionDecisionTestResult.objects.filter(user=request.user).last()
    # last_result = ReactionDecisionTestResult.objects.filter(user=request.user).first()
    success_for_next_level = 4
    # next_level = False
    # first_level = {
    #     'level': 1,
    #     'balls': 12,
    #     'speed': 3,
    #     'red_balls': 4,
    # }
    #
    # if (first_result and last_result):
    #     last_results = ReactionDecisionTestResult.objects.filter(user=request.user)[0:success_for_next_level]
    #     if len(last_results) >= success_for_next_level:
    #         for result in last_results:
    #             if not result.success or result.level != last_result.level:
    #                 next_level = False
    #                 break
    #             next_level = True
    #
    #     balls_level = last_result.balls-first_result.balls
    #     speed_level = last_result.speed-first_result.speed
    #     red_balls_level = last_result.red_balls-first_result.red_balls
    #     current_level = {
    #         'level': last_result.level,
    #         'balls': last_result.balls,
    #         'speed': last_result.speed,
    #         'red_balls': last_result.red_balls,
    #     }
    #
    #     if next_level:
    #         if balls_level > speed_level:
    #             current_level['speed'] += 1
    #         elif speed_level > red_balls_level:
    #             current_level['red_balls'] += 1
    #         else:
    #             current_level['balls'] += 1
    #         current_level['level'] += 1
    # else:
    #     current_level = first_level

    results = ReactionDecisionTestResult.objects.filter(user=request.user)[0:30].values()
    for result in results: result["created_at"] = result["created_at"].astimezone(timezone.get_default_timezone()).strftime('%d/%m/%Y, %H:%M')
    return Response({
        'username': request.user.username,
        'current_level': first_level,
        'success_for_next_level': success_for_next_level,
        # 'first_result': first_result,
        # 'last_result': last_result,
        'results': list(results)
    }, status=HTTP_200_OK)
