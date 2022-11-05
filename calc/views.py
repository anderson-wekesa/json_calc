from rest_framework.parsers import JSONParser
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .serializers import OperationSerializer


class CalculatorClass():
    http_method_names = ['post', 'options']

    @csrf_exempt
    def Calculate(request):
        header = {"Access-Control-Allow-Origin":"*"}

        if request.method == 'POST':
            data = JSONParser().parse(request) #Parse the JSON input
            serializer = OperationSerializer(data = data)
    
            if serializer.is_valid():
                serializer.save() #Save Operation
                op_type = serializer.data.get('operation_type') #Determine operation type
                x_val = serializer.data.get('x') #Retrieve X value
                y_val = serializer.data.get('y') #Retrieve Y value

                #Perform Calculation
                if (op_type == 'addition'):
                    result = x_val + y_val
                elif (op_type == 'subtraction'):
                    result = x_val - y_val
                elif (op_type == 'multiplication'):
                    result = x_val * y_val
                
                response = {'slackUsername':'callmeanderson', 'operation_type':op_type, 'result':result}
                return JsonResponse(response, status = 201, headers = header)
            return JsonResponse(serializer.errors, status = 400, headers = header) #return error
        else:
            return HttpResponse("Successfull GET!")