from django.db.models import Sum
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.views import APIView
from apiv1.models import SubmittedExam
from apiv1.exceptions import ResultNotFound


class ResultViewSet(APIView):
	
	def get(self, request, pk,format = None):
		check_score = SubmittedExam.objects.filter(user_id = pk).aggregate(Sum('score'))
		if check_score['score__sum'] is None:
			raise ResultNotFound("Couldn't find result")
		else:
			print(check_score['score__sum'])
			if int(check_score['score__sum']) > 0:
				result = 'pass'
			else:
				result = 'fail'
		return Response({'result':result})
