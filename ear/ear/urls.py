"""ear URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path, re_path
from user.views import LoginView, RegisterView, index, logout, annotation
from predict.views import PredictView
from django.conf import settings
from django.conf.urls.static import static
from board.views import BoardView


urlpatterns = [
    path('', index),
    path('predict/', PredictView.as_view()),
    path('logout/', logout),
    path('admin/', admin.site.urls),
    path('login/', LoginView.as_view()),
    path('register/', RegisterView.as_view()),
    path('annotation/', annotation),
    path('board/', BoardView.as_view()),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
