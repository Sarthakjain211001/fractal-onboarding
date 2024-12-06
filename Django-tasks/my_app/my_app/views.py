from django.http import HttpResponse

def welcome_page(request):
    return HttpResponse("Welcome to Django-tasks app sarthak !!!")