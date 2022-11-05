from rest_framework import serializers
from .models import Operation, OpResponse

class OperationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Operation
        fields = ('operation_type', 'x', 'y')

class OpResponseSerializer(serializers.ModelSerializer):
    class Meta:
        model = OpResponse
        fields = ('slackUsername', 'operation_type', 'result')