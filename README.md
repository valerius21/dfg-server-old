# DFG API

## Configure

## Starting the instance

### Docker

Pull: `docker pull docker.gitlab.gwdg.de/dfg/api:latest`

Start: `docker run --restart always --name api -d -p 80:8000 -v config.yml:/dfg_server/etc/config.yml:ro dfg-api:latest`

### Python

**[WIP]**
