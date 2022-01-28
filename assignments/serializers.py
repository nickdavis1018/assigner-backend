from assignments.models import Assignment
from rest_framework.serializers import ModelSerializer, HyperlinkedModelSerializer
from django.contrib.auth.models import User, Group

class AssignmentSerializer(ModelSerializer):
    class Meta:
        model = Assignment
        fields = ["id", "task", "assignee", "notes", "completed", "urgency", "assigner", "overdue", "flagged"]