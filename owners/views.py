from django.shortcuts import render

# Create your views here.
import json

from django.http import JsonResponse
from django.views import View

from owners.models import Owner, Dog

class OwnersView(View):
    def post(self, request):
        data = json.loads(request.body)
        owner = Owner.objects.create(
            name = data['name'],
            email = data['email'],
            age = data['age']
            )
        return JsonResponse({'MESSAGE':'CREATED'}, status=201)

class DogsView(View):
    def post (self, request):
        data = json.loads(request.body)
        dog = Dog.objects.create(
            name = data['dog_name'],
            age = data['dog_age'],
            owner = Owner.objects.get(name=data['owner_name'])
        )

        return JsonResponse({'MESSAGE':'CREATED'}, status=201)