from django.shortcuts import render, HttpResponse
from django.views import View
from auth_app.models import Users
from auth_app import forms
import bcrypt
import uuid

sessions=dict()

def authorization(request):
    session_code = request.COOKIES.get('session_code')
    user_id = sessions.get(session_code,None)
    return user_id

class LogOut(View):

    def get(self,request) -> HttpResponse:

        if authorization(request) is None:
            return HttpResponse("Чтобы выйти, нужно сначала войти")
        
        session_code = request.COOKIES.get('session_code')
        sessions.pop(session_code)

        responce = HttpResponse(sessions)
        responce.delete_cookie(key=session_code)

        return responce

class Registration(View):
    

    def get(self, request) -> render:
        form = forms.LoginForm()
        return render(request,'auth_app/login.html', {'form':form})
    
    def post(self,request) -> HttpResponse:
        login = request.POST['login']
        salt = bcrypt.gensalt()
        password = bcrypt.hashpw(request.POST['password'].encode('utf-8'),salt)
        user = Users(Login = login, Password = password.decode('utf-8'))
        user.save()
        return HttpResponse('Sucsess')
    
class Authentication(View):
    def get(self,request) -> render:
        form = forms.SignUpForm()
        return render(request,'auth_app/sign-up.html', {'form':form})
    
    def post(self,request) -> HttpResponse:
        login = request.POST['login']
        password = request.POST['password'].encode('utf-8')
        user = Users.objects.get(Login = login)
        correct_password = user.Password.encode('utf-8')
        if bcrypt.checkpw(password,correct_password):
            session_code = str(uuid.uuid4())
            sessions[session_code] = user.ID
            print(sessions)
            responce = HttpResponse(sessions)
            responce.set_cookie(key = 'session_code',value=session_code, max_age=999999)
        return responce 
    
