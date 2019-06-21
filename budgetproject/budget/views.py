from django.shortcuts import render

def project_list(request):
    # template name
    return render(request, 'budget/project-list.html')

def project_detail(request, project_slug):
    # fetch the correct project from urls
    return render(request, 'budget/project-detail.html')
