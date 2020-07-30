from gql import Client

class GithubClient:
    def __init__(self, token):
        self.client = Client(transport=RequestsHTTPTransport(
            url='/graphql'
        headers = {'Authorization': 'token'}),
        schema = schema)
        query = gql('''
        {
          hello
        }
        ''')

        client.execute(query)

        self.client = Client()

    def get_teams(self, organization):


