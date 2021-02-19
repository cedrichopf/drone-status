class DroneBuild:
  def __init__(self, host, protocol, repository, build):
    super().__init__()
    self.host = host
    self.protocol = protocol
    self.repository = repository
    self.build = build

  def generate_target_url(self):
    return self.protocol + "://" + self.host + "/" + self.repository + "/" + self.build
