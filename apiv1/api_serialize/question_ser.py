from rest_framework import serializers
from apiv1.models import Questions
from apiv1.models import SubmittedExam

class QuestionsSerializer(serializers.ModelSerializer):
	class Meta:
		model = Questions
		fields = ('question', 'description',
					 'answer_a', 'answer_b', 'answer_c', 'answer_d','answer_e')


class SubmittedExamSerializer(serializers.ModelSerializer):
	# question_detail = serializers.RelatedField(source = 'question', read_only=True)
	class Meta:
		model = SubmittedExam
		fields = ('user_answer', 'question')


	def create(self, validate_data):
		check_anwer = Questions.objects.get(pk = validate_data['question'].pk)
		is_correct = check_anwer.correct_answer == validate_data['user_answer']
		score = 1 if is_correct == True else 0
		exam =  SubmittedExam.objects.create(user = self.context['request'].user, 
			user_answer = validate_data['user_answer'], 
			is_correct = is_correct, score = score, question = validate_data['question'])
		exam.save()
		return exam