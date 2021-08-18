from typing import AsyncGenerator
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

    def get(self, request):
        owners = Owner.objects.all()
        results = []
        for owner in owners:
            dogs = owner.dog_set.all()
            dogs_list = []
            for dog in dogs:
                dogs_list.append(
                    {
                        "dog_name" : dog.name,
                        "dog.age" : dog.age
                    }
                )
            results.append(
            {
                "name" : owner.name,
                "email": owner.email,
                "age" : owner.age,
                "dogList" : dogs_list
            }
        )
    
        return JsonResponse({'results':results}, status=200)

class DogsView(View):
    def post (self, request):
        data = json.loads(request.body)
        dog = Dog.objects.create(
            name = data['dog_name'],
            age = data['dog_age'],
            owner = Owner.objects.get(name=data['owner_name'])
        )

        return JsonResponse({'MESSAGE':'CREATED'}, status=201)

    def get(self, request):
        dogs = Dog.objects.all()
        results = []
        print(dogs)
        for dog in dogs:
            results.append(
                {
                    # "owner_name": Owner.objects.get(id=dog.owner_id).name,
                    "owner_name": dog.owner.name,
                    "dog_name": dog.name,
                    "age": dog.age,
                }
            )
        
        return JsonResponse({'results':results}, status=200)