from django.urls import path
from contacts import views

urlpatterns = [
    path('api/contacts/', views.ContactListCreate.as_view()),
]