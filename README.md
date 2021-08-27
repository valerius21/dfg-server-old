# DFG API

Currently, Sync Only!

## Configure

provide a `/etc/config.yml` accordingly.

## Starting the instance

### Docker

Pull: `docker pull docker.gitlab.gwdg.de/dfg/api:latest`

Start: `docker run --restart always --name api -d -p 80:8000 -v config.yml:/dfg_server/etc/config.yml:ro dfg-api:latest`

### Python

**[WIP]**

### Planned

- Async requests
- Auth
- CI/CD Pipeline
