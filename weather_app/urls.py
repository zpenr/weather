from django.urls import path
from weather_app import views
urlpatterns = [
    path('',views.IndexPage.as_view()),
]