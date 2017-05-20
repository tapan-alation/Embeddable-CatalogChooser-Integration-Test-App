import json
import requests

from django.views.decorators.csrf import csrf_exempt
from django.views.generic import TemplateView
from django.http import JsonResponse


class RegisterOpenerView(TemplateView):
    template_name = 'register_opener.html'

    @csrf_exempt
    def post(self, request):
        alation_object_receiver_endpoint = request.build_absolute_uri('/alation_object_receiver/')
        alation_url = request.POST.get("alationBaseURL")
        alation_api_token = request.POST.get("alationAPIToken")
        app_name = request.POST.get("appName")
        accept_object_types = request.POST.get("acceptObjectTypes").split(",")
        accept_data_source_types = request.POST.get("acceptDataSourceTypes").split(",")

        alation_url += '/' if alation_url[-1] != '/' else ''
        alation_register_opener_endpoint = alation_url + 'integration/catalog_chooser/register_opener/'
        payload = {
            "endpoint": alation_object_receiver_endpoint,
            "name": app_name,
            "accept_object_types": accept_object_types,
            "accept_data_source_types": accept_data_source_types
        }
        headers = {
            "TOKEN": alation_api_token,
            "Content-Type": "application/json"
        }
        alation_resp = requests.post(alation_register_opener_endpoint, data=json.dumps(payload), headers=headers)
        return JsonResponse(json.dumps(alation_resp.content), safe=False)


