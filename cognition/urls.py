"""cognition URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('articles.urls')),
    path('balls/', include('balls.urls')),
    path('reaction_test/', include('reaction_test.urls')),
    path('reaction_decision_test/', include('reaction_decision_test.urls')),
    path('keyboard_mouse_coordination/', include('keyboard_mouse_coordination.urls')),
    path('mouse_tracking/', include('mouse_tracking.urls')),
    path('api/v0/', include('api_v0.urls')),
]
