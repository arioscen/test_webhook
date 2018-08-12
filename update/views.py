from django.http import HttpResponse, HttpResponseForbidden
from django.views.decorators.csrf import csrf_exempt
from django.utils.encoding import force_bytes
import hmac
import hashlib


@csrf_exempt
def update(request):
    http_x_github_event = request.META.get('HTTP_X_GITHUB_EVENT', '')
    http_x_hub_signature = request.META.get('HTTP_X_HUB_SIGNATURE', '')
    sha_name, signature = http_x_hub_signature.split('=')

    if http_x_github_event == 'ping':
        return HttpResponse('Success')
    elif http_x_github_event == 'push':
        mac = hmac.new(force_bytes('test123'), msg=force_bytes(request.body), digestmod=hashlib.sha1)
        if not hmac.compare_digest(force_bytes(mac.hexdigest()), force_bytes(signature)):
            return HttpResponseForbidden('Permission denied.')

        # do something
        with open('/tmp/update.log', 'w') as f:
            f.write(http_x_github_event+'\n'+signature)

    return HttpResponse('Success')
#