import json
from django.http import HttpResponse
from django.conf import settings
import jwt

class jwt_auth(object):
    def process_request(self,request):
        if request.path == settings.LOGIN_PATH:
            return None

        jwt_token = request.META.get('HTTP_AUTHORIZATION')

        try:
            payload = jwt.decode(jwt_token, settings.JWT_SECRET,algorithms=[settings.JWT_ALGORITHM])
            print(payload)
        except (jwt.DecodeError, jwt.ExpiredSignatureError):
            return HttpResponse(json.dumps({'message': 'Token is invalid'}), content_type="application/json")       
        request.user = payload['user']
        return None
