import os, requests
from config import config
from github import github
from drone import build

def main():
  cfg = config.Config()
  client = github.GitHubClient(cfg.api_token, cfg.endpoint, cfg.repository, cfg.commit)
  drone = build.DroneBuild(cfg.drone_host, cfg.drone_protocol, cfg.drone_repository, cfg.drone_build)
  body = {
    "state": os.getenv("PLUGIN_STATE"),
    "target_url": drone.generate_target_url(),
    "description": os.getenv("PLUGIN_DESCRIPTION"),
    "context": os.getenv("PLUGIN_CONTEXT")
  }
  client.create_status(body)

main()
