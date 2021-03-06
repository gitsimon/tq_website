from django.http import Http404
from rest_framework import generics, permissions
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import *


class SurveyDetail(generics.RetrieveAPIView):
    model = Survey
    serializer_class = SurveySerializer
    queryset = Survey.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]

class SurveyAnswer(APIView):
    """
    Change if a subscription is paid/not paid
    """
    permission_classes = [
        permissions.AllowAny
    ]

    def get_object(self, pk):
        try:
            s = Answer.objects.get(pk=pk)
        except Answer.DoesNotExist:
            raise Http404
        self.check_object_permissions(self.request, s)
        return s

    def get(self, request, pk, format=None):
        s = self.get_object(pk)
        serializer = AnswerSerializer(s)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        s = self.get_object(pk)
        serializer = AnswerSerializer(s, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

