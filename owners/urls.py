from django.urls import path
from django.urls.resolvers import URLPattern
from owners.views import OwnersView, DogsView

urlpatterns = [
    path('register-owner', OwnersView.as_view()),
    path('register-dog', DogsView.as_view()),
]