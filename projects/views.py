from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.core.paginator import Paginator

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

@login_required
def project_edit(request, project_id):
    project = get_object_or_404(Project, id=project_id)

    if request.user.is_anonymous or request.user != project.owner:
        return redirect('projects:detail', project_id)

    if request.method == 'POST':
        form = ProjectForm(request.POST, instance=project)
        if form.is_valid():
            form.save()
        return redirect('projects:detail', project_id)

    form = ProjectForm(instance=project)
    context = {
        'form': form
    }
    return render(request, 'projects/create-project.html', context)

@login_required
def project_complete(request, project_id):
    pass

def project_detail(request, project_id):
    template = 'projects/project-details.html'

    project = get_object_or_404(Project, id=project_id)

    if project is None:
        raise Http404('Error')
    elif project.status == 'closed':
        if project.author != request.user:
            raise Http404('Error')

    context = {
        'project': project,
    }
    return render(request, template, context)

def skill_remove(request, project_id, skill_id):
    pass

def skill_add(request):
    pass

def skill_search(request, skill_name):
    pass
