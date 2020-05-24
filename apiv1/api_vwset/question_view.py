from rest_framework import viewsets
from rest_framework.response import Response
from apiv1.api_serialize.question_ser import QuestionsSerializer
from apiv1.models import Questions

class QueViewSet(viewsets.ModelViewSet):

	queryset = Questions.objects.all()
	serializer_class = QuestionsSerializer

