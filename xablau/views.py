import json
from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime, timedelta
from django.views.decorators.csrf import csrf_exempt
import jwt
from django.conf import settings


USUARIO = "mohammed"
SENHA = "xarulei"
RESPOSTA_LDAP = True


# Create your views here.
def hello(request):
    return HttpResponse("hello")

@csrf_exempt
def login(request):
    if request.method == "POST":
        json_data = json.loads(request.body) 
        login_user = json_data['user']
        login_pass = json_data['pass'] 
        ########### CONSULTA LDAP #########       
        if RESPOSTA_LDAP == True:
            payload = {
                'user': login_user,
                'exp': datetime.utcnow() + timedelta(seconds=settings.JWT_EXP_DELTA_SECONDS)
            }
            jwt_token = jwt.encode(payload, settings.JWT_SECRET, settings.JWT_ALGORITHM)
            return HttpResponse(json.dumps({'token': jwt_token.decode('utf-8')}), content_type="application/json")       
    else:
        return HttpResponse(json.dumps({'error':'500'}), content_type="application/json")       

