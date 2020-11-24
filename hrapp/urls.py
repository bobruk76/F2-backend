from django.contrib import admin
from django.urls import path
# from hrapp.serializers import QuestionSerializer

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

app_name = 'hrapp'

urlpatterns = [
    path('admin/', admin.site.urls),

    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

# question
#     path('api/question/', QuestionSerializer.as_view(), name='question-list'),

]
