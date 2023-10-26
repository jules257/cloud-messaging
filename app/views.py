from django.shortcuts import render


# Create your views here.
from rest_framework import views
from rest_framework.response import Response
from rest_framework import views
from rest_framework.response import Response
from rest_framework import status
from firebase_admin import messaging

class SendFCMNotificationView(views.APIView):
    def post(self, request):
        message = request.data.get('message')
        registration_token = request.data.get('registration_token')

        # Créez un message FCM
        message = messaging.Message(
            notification=messaging.Notification(
                title='Titre de la notification',
                body=message,
            ),
            token=registration_token,
        )

        # Envoyez le message
        response = messaging.send(message)

        return Response({'status': 'Notification envoyée avec succès'}, status=status.HTTP_200_OK)


