# Drone CI Plugin for GitHub Status

- [Drone CI Plugin for GitHub Status](#drone-ci-plugin-for-github-status)
  - [Overview](#overview)
  - [Usage](#usage)
  - [Settings](#settings)
  - [Environment Variables](#environment-variables)

---

## Overview

This plugin creates/updates a GitHub status for a given repository and commit hash.

## Usage

```yaml
---
kind: pipeline
type: docker
name: github-status

trigger:
  event:
    - pull_request

steps:
  - name: create-status
    image: cedrichopf/drone-status
    settings:
      api_token: 1234567890
      state: success
      context: drone-ci/status-plugin
      description: Build successful
```

## Settings

```yaml
settings:
  api_token: 1234567890
  state: success
  context: drone-ci/status-plugin
  description: Build successful
  repo: cedrichopf/drone-status
  commit: 9f11f66aa4a7338ced215fb212d16e12b0edce46
  endpoint: https://github.enterprise.com
```

All settings will be passed into the container using environment variables. A complete overview of the available
environment variables can be found in the table below.

## Environment Variables

The following table contains an overview of the available environment variables to configure the application.

| Name               | Description                                                   | Default Value            |
| ------------------ | ------------------------------------------------------------- | ------------------------ |
| PLUGIN_API_TOKEN   | Access token to interact with the GitHub API                  | `-`                      |
| PLUGIN_STATE       | State of the status: `error`, `failure`, `pending`, `success` | `-`                      |
| PLUGIN_CONTEXT     | Status context, e.g. `drone/status-plugin`                    | `-`                      |
| PLUGIN_DESCRIPTION | Status description, e.g. `Build is pending`                   | `-`                      |
| PLUGIN_REPO        | Target repository to set the status                           | Pipeline repository      |
| PLUGIN_COMMIT      | Status' commit hash                                           | Pipeline commit          |
| PLUGIN_ENDPOINT    | Endpoint of the GitHub instance (e.g. GitHub Enterprise)      | `https://api.github.com` |
