from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.throttling import UserRateThrottle
from .models import Waitlist
from rest_framework.permissions import AllowAny
from django.core.validators import validate_email
from django.core.exceptions import ValidationError


# Create your views here.
class WaitlistAPI(APIView):
    throttle_classes = [UserRateThrottle]
    permission_classes = (AllowAny,)

    def post(self, request, *args, **kwargs):
        email = request.data.get('email', None)

        if not email:
            return Response({'detail': 'No email provided'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            validate_email(email)
        except ValidationError:
            return Response({'detail': 'Invalid email provided'}, status=status.HTTP_400_BAD_REQUEST)

        # check if email has the correct format

        waitlist, _ = Waitlist.objects.get_or_create(email=email)

        return Response({'detail': f'{waitlist.email} added to waitlist'}, status=status.HTTP_201_CREATED)
