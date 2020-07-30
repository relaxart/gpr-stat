import os

from gql import Client, gql
from gql.transport.requests import RequestsHTTPTransport


class GithubClient:
    def __init__(self, token):
        transport = RequestsHTTPTransport(
            url='https://api.github.com/graphql',
            headers={'Authorization': 'bearer {token}'.format(token=token)},
            retries=3,
        )

        self.client = Client(
            transport=transport,
            fetch_schema_from_transport=True,
        )

    def get_teams(self, organization):
        path = os.getcwd() + "/octototoro/queries/teams.graphql"
        f = open(path, "r")
        query = f.read().replace('%login%', organization)
        data = self.client.execute(gql(query))
        for x in data['organization']['teams']['edges']:
            print(x)
