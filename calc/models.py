from django.db import models
from enum import Enum

# Create your models here.
class OperationTypes(Enum):
    addition = "addition"
    subtraction = "subtraction"
    multiplication = "multiplication"


class Operation(models.Model):
    operation_type = models.CharField(max_length = 20, choices = [(op.name, op.name) for op in OperationTypes], default=OperationTypes("addition").name, blank = False)
    x = models.IntegerField(default = 0, blank = False)
    y = models.IntegerField(default = 0, blank = False)