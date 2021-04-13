from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status, viewsets
from rest_framework.decorators import api_view

from .models import Todo
from .serializers import TodoSerializer


@api_view(['GET'])  # GET 으로 요청 시 응답
def status_check(request):
    """
    서버의 상태를 확인하는 함수
    """
    return Response({
        "status": "OK"
    }, status=status.HTTP_200_OK)


# ModelViewSet -> Create, Retrieve, Update, Partial_update, Destroy, List 지원
class TodoModelViewSet(viewsets.ModelViewSet):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
