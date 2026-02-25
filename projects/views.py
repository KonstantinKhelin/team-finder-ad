from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.core.paginator import Paginator
#from django.views.generic.edit import CreateView
#from django.urls import reverse_lazy

from .models import Project, Skill
from .forms import ProjectForm

def project_list(request):
    template = 'projects/project_list.html'

    projects = Project.objects.all().filter(status='open')

    paginator = Paginator(projects, 12)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'projects': page_obj
    }
    return render(request, template, context)

#class ProjectCreate(CreateView):
#    model = Project
#    form_class = ProjectForm
#    template_name = 'projects/create-project.html'
#    success_url = reverse_lazy('list')

@login_required
def project_create(request):
    form = ProjectForm(request.POST or None,)
    if form.is_valid():
        obj = form.save(commit=False)
        obj.owner = request.user
        form.save()
        return redirect('/projects/list/')
    context = {'form': form}
    return render(request, 'projects/create-project.html', context)

def project_edit(request, post_id):
    pass
#    post = get_object_or_404(Post, id=post_id)
#
#    if request.user.is_anonymous or request.user != post.author:
#        return redirect('blog:post_detail', post_id)
#
#    if request.method == 'POST':
#        form = PostForm(request.POST, files=request.FILES, instance=post)
#        if form.is_valid():
#            form.save()
#        return redirect('blog:post_detail', post_id)
#
#    form = PostForm(instance=post)
#    context = {
#        'form': form
#    }
#    return render(request, 'blog/create.html', context)

@login_required
def project_complete(request, post_id):
    pass

def project_detail(request, project_id):
    pass

def project_edit(request, project_id=-1):
    pass

def project_complete(request, project_id):
    pass

def skill_remove(request, project_id, skill_id):
    pass

def skill_add(request):
    pass

def skill_search(request, skill_name):
    pass
