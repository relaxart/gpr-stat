from django.shortcuts import render
from octototoro.github.client import GithubClient


def index(request):
    return render(request, 'index.html', {'repos': {}})


def repo(request, owner, name):
    client = GithubClient("")
    client.get_teams(owner)
    return render(request, 'repo.html', {'repo': repo, 'prs': {}, 'contributors': {}})
