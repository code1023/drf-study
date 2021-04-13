from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import *

# viewset 은 router 를 사용하여 URL 을 관리할 수 있습니다.
router = DefaultRouter()
router.register(r'todo', TodoModelViewSet)

urlpatterns = [
    # /api/status_check/
    path("status_check/", status_check, name="status_check"),
    # /api/todo/
    path('', include(router.urls)),     # 위에 선언한 router 를 사용
]
