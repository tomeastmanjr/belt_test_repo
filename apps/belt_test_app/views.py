from django.shortcuts import render, HttpResponse, redirect
from .models import People

def index(request):
    context = { "somekey":"somevalue" }
    People.objects.create(first_name='Tom', last_name='Eastman')
    people = People.objects.all()
    print (people)
    return render(request, 'belt_test_app/index.html', context)

def show(request):
    print(request.method)
    return render(request, 'belt_test_app/show_users.html')
