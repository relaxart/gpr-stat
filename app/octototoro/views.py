from django.shortcuts import render
from github import Github


def index(request):
    return render(request, 'index.html', {'repos': {}})


def repo(request, owner, name):

    return render(request, 'repo.html', {'repo': repo, 'prs': {}, 'contributors': {}})
