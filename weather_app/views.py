from django.shortcuts import render, HttpResponse
from django.views import View

class IndexPage(View):
    def get(self, request):
        return render(request,'weather_app/index.html')