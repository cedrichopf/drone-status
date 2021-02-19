import requests

class GitHubClient:
  def __init__(self, token, endpoint, repository, commit):
    super().__init__()
    self.token = token
    self.endpoint = endpoint
    self.repository = repository
    self.commit = commit

  def create_status(self, body):
    url = self.__generate_url()
    headers = self.__get_headers()
    response = requests.post(url, headers=headers, json=body)

  def __generate_url(self):
    return self.endpoint + "/repos/" + self.repository + "/statuses/" + self.commit

  def __get_headers(self):
    return {
      "Authorization": "token " + self.token
    }
