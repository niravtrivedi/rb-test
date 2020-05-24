from rest_framework import serializers
from apiv1.models import Questions
from apiv1.models import SubmittedExam

class QuestionsSerializer(serializers.Serializer):
	result = serializers.CharField(max_length = 10)