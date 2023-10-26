from django.urls import path
from .views import SendFCMNotificationView
from .tests import TestTokenView







urlpatterns = [
    path('send-notification/',SendFCMNotificationView.as_view(),name='send-notification'),
    path('test-token/', TestTokenView.as_view(), name='test-token'),

   
]




