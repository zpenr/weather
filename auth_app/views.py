from django.shortcuts import render, HttpResponse
from django.views import View
from auth_app.models import Users
import bcrypt
class Login(View):
    def get(self, request):
        return render(request,'auth_app/login.html')
    
    def post(self,request):
        login = request.POST['login']
        salt = bcrypt.gensalt()
        password = bcrypt.hashpw(request.POST['password'].encode('utf-8'),salt)
        user = Users(Login = login, Password = password)
        user.save()
        return HttpResponse('Sucsess')