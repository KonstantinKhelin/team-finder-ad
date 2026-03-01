from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView

from projects.models import Project
from .forms import CustomAuthenticationForm, CustomUserForm
from .models import CustomUser

def profile(request, user_id):
    profile = get_object_or_404(CustomUser, id=user_id)
    context = {'user': profile}
    return render(request, 'users/user-details.html', context)

def user_list(request):
    template = 'users/participants.html'

    users = CustomUser.objects.all().filter(is_active=True).order_by('-id')

    paginator = Paginator(users, 12)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        "participants": page_obj
    }
    return render(request, template, context)

def register(request):
    pass

@login_required
def edit_profile(request):
    if request.method == 'POST':
        form = CustomUserForm(request.POST or None, instance=request.user)

        if form.is_valid():
            form = form.save(commit=False)
            form.save()
            return redirect('/projects/list/')

    form = CustomUserForm(instance=request.user)

    context = {
        'form': form
    }
    return render(request, 'users/edit_profile.html', context)

class CustomLoginView(LoginView):
    authentication_form = CustomAuthenticationForm
    template_name = 'users/login.html'
    success_url = '/projects/list/'

    def form_valid(self, form):
        login(self.request, form.get_user())
        return super().form_valid(form)

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['request'] = self.request  # Передаём request в форму
        return kwargs

def custom_logout(request):
    logout(request)
    return redirect('/projects/list/')
