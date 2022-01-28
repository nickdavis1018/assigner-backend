from django.shortcuts import render
from django.contrib.auth.models import User, Group
from assignments.models import Assignment
from assignments.serializers import AssignmentSerializer
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework_simplejwt.authentication import JWTAuthentication

# Create your views here.

class AssignmentViews(ModelViewSet):
    queryset = Assignment.objects.all()
    serializer_class = AssignmentSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = (JWTAuthentication,)
# Create your views here.
