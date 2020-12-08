from django.contrib import admin
from django.urls import path, include, re_path
from .views import QuestionView, TestingView, QuestionnaireList, questionnaire_detail

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

app_name = 'hrapp'

urlpatterns = [
    re_path(r'^tinymce/', include('tinymce.urls')),

    path('admin/', admin.site.urls),

    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    path('api/question/', QuestionView.as_view(), name='questions'),

    path('api/questionnaire/', QuestionnaireList.as_view(), name='questionnaires_list'),
    path('api/questionnaire/<uuid:pk>', questionnaire_detail, name='questionnaires_view'),

    path('api/results/', TestingView.as_view(), name='results'),
    path('api/results/<int:pk>', TestingView.as_view(), name='results'),

]
