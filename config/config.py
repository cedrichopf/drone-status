import os

class Config:
  def __init__(self):
    super().__init__()
    self.api_token = os.getenv("PLUGIN_API_TOKEN")
    self.endpoint = self.__plugin_endpoint()
    self.repository = self.__plugin_repository()
    self.commit = self.__plugin_commit()
    self.drone_host = os.getenv("DRONE_SYSTEM_HOST")
    self.drone_protocol = os.getenv("DRONE_SYSTEM_PROTO")
    self.drone_repository = os.getenv("DRONE_REPO")
    self.drone_build = os.getenv("DRONE_BUILD_NUMBER")

  def __plugin_endpoint(self):
    custom_endpoint = os.getenv("PLUGIN_ENDPOINT")
    if custom_endpoint:
      return custom_endpoint
    return "https://api.github.com"

  def __plugin_repository(self):
    custom_repository = os.getenv("PLUGIN_REPO")
    if custom_repository:
      return custom_repository
    return os.getenv("DRONE_REPO")

  def __plugin_commit(self):
    custom_commit = os.getenv("PLUGIN_COMMIT")
    if custom_commit:
      return custom_commit
    return os.getenv("DRONE_COMMIT")
