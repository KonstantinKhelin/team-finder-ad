from django.core.paginator import Paginator


def paginate_queryset(queryset, request, per_page=12, page_param='page'):
    paginator = Paginator(queryset, per_page)
    page_number = request.GET.get(page_param)
    page_obj = paginator.get_page(page_number)
    return page_obj

def check_project_owner(request, project):
    if request.user != project.owner:
        raise PermissionDenied
