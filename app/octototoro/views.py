from django.shortcuts import render
from octototoro.github.client import GithubClient


def index(request):
    return render(request, 'index.html', {'repos': {}})


def repo(request, owner, name):
    client = GithubClient("fc6ea9740dfbdc2c2b36972d10b77e271664ecb0")
    client.get_teams(owner)
    return render(request, 'repo.html', {'repo': repo, 'prs': {}, 'contributors': {}})
