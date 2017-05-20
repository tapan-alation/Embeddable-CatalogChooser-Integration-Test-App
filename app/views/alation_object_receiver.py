import json

from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.http import JsonResponse


ALATION_DATA = {}

@csrf_exempt
def endpoint(request):
    if request.method.lower() == 'post':
        global ALATION_DATA 
        ALATION_DATA = request.POST.dict()
        response = {"location": request.build_absolute_uri()}
        return JsonResponse(response)
    else:
        global ALATION_DATA
        return JsonResponse(ALATION_DATA)