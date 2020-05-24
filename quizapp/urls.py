"""quizapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from rest_framework import routers
from apiv1.api_vwset.question_view import QueViewSet
from apiv1.api_vwset.submitanswer_view import SubmitAnswerViewSet
from apiv1.api_vwset.result_view import ResultViewSet

router = routers.DefaultRouter()
# router.register(r'questions', QueViewSet)

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url('', include(router.urls)),
    url(r'questions', QueViewSet.as_view({'get': 'list'})),
    url(r'quiz-answer', SubmitAnswerViewSet.as_view({'post': 'create','get': 'list'})),
    url(r'api-auth/', include('rest_framework.urls')),
    url(r'result/(?P<pk>[^/.]+)/$', ResultViewSet.as_view()),
]