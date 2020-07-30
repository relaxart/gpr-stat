from django.shortcuts import render
from github import Github


def index(request):
    g = Github("")
    return render(request, 'index.html', {'repos': g.get_user().get_repos()})


def repo(request, owner, name):
    g = Github("")
    repo = g.get_repo(owner + '/' + name)
    contributors = repo.get_contributors()
    prs = repo.get_pulls('all')

    return render(request, 'repo.html', {'repo': repo, 'prs': prs.get_page(0), 'contributors': contributors})
