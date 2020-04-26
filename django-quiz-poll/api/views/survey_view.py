from rest_framework import generics

from ..serializers import SurveySerializer


class SurveyView(generics.CreateAPIView):
    serializer_class = SurveySerializer

    def perform_create(self, serializer):
        serializer.save()
