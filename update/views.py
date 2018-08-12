from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def update(request):
    http_x_github_event = request.META.get('HTTP_X_GITHUB_EVENT', '')
    http_x_hub_signature = request.META.get('HTTP_X_HUB_SIGNATURE', '')
    with open('/tmp/update.log', 'a') as f:
        f.write(http_x_github_event+'/n'+http_x_hub_signature)
    return HttpResponse('Success')

##