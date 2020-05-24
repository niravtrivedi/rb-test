from rest_framework import viewsets
from rest_framework.response import Response
from apiv1.api_serialize.question_ser import SubmittedExamSerializer
from apiv1.models import Questions
from apiv1.models import SubmittedExam



class SubmitAnswerViewSet(viewsets.ModelViewSet):
	serializer_class = SubmittedExamSerializer
	def get_queryset(self):
		return SubmittedExam.objects.filter(user = self.request.user)
