from django.shortcuts import render

from django.views import View
from django.http import JsonResponse

from .models import Movie
# Create your views here.
class MovieView(View):
    def get(self, request):
        return JsonResponse({"results" : [{
                "title" : movie.title,
                "running_time" : movie.running_time,
                "actor_list" : [{
                    "first_name" : actor.first_name,
                    "last_name" : actor.last_name,
                } for actor in movie.actors.all()]
            } for movie in Movie.objects.all()]}, status=201)