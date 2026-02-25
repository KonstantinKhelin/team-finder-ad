from django.shortcuts import render
from django.core.paginator import Paginator

from .models import User

def profile(request, user_id):
    pass

def user_list(request):
    template = 'users/participants.html'

    users = User.objects.all().filter(is_active=True).order_by('-id')

    paginator = Paginator(users, 12)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        "participants": page_obj
    }
    return render(request, template, context)

def register(request):
    pass

def edit_ptofile(request):
    pass
