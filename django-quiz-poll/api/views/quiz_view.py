from rest_framework import generics
from ..serializers import QuizSerializer


class QuizView(generics.CreateAPIView):
    serializer_class = QuizSerializer

    def perform_create(self, serializer):
        serializer.save()

