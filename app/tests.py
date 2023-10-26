from django.test import TestCase

# Create your tests 
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class TestTokenView(APIView):
    def get(self,request):
        test_token = "VOTRE_JETON_FICTIF_DE_TEST"
        return Response({'test_token':test_token},status=status.HTTP_200_OK)


