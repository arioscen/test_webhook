from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json


@csrf_exempt
def update(request):
    http_x_github_event = request.META.get('HTTP_X_GITHUB_EVENT', '')
    http_x_hub_signature = request.META.get('HTTP_X_HUB_SIGNATURE', '')
    json_data = json.loads(request.body)
    repo_data = json_data.get('repository', '')
    sender_data = json_data.get('sender', '')
    if repo_data and sender_data and http_x_hub_signature:
        user_id = sender_data.get('id', '')
        user_name = sender_data.get('login', '')
        repo_name = repo_data.get('name', '')
        repo_id = repo_data.get('id', '')
        repo_ssh_url = repo_data.get('ssh_url', '')
        sha_name, signature = http_x_hub_signature.split('=')
    with open('/tmp/update.log', 'a') as f:
        f.write(http_x_github_event+'/n'+http_x_hub_signature)
    return HttpResponse('Success')

