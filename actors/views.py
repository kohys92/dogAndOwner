from django.shortcuts import render

from django.views import View
from django.http import JsonResponse

from .models import Actor
# Create your views here.

class ActorView(View):
    def get(self, request):
        return JsonResponse({"results" : 
        [{  "id" : actor.id,
            "first_name" : actor.first_name,
            "last_name" : actor.last_name,
            "date_of_birth" : actor.date_of_birth,
            "movies" : 
            [{  "title" : movie.title,
                "release_date" : movie.release_date,
                "running_time" : movie.running_time,
            } for movie in actor.movies.all()],
        } for actor in Actor.objects.all()]},
        status=200)