FROM python:3.9-slim-buster

RUN apt-get update && apt-get upgrade -y

WORKDIR /dfg_server

COPY requirements.txt ./

RUN pip3 install --no-cache-dir -r requirements.txt

COPY . .

ENV PYTHONPATH=$PYTHONPATH:/dfg_server
ENV DFG_PRODUCTION=True

CMD ["python3", "/dfg_server/cli/server.py"]
