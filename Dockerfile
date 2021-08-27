FROM python:3.9-slim-buster

WORKDIR /dfg_server

COPY requirements.txt ./

RUN pip3 install --no-cache-dir -r requirements.txt

COPY . .

ENV DFG_CONFIG=/dfg_server/etc/prod_config.yml
ENV PYTHONPATH=$PYTHONPATH:/dfg_server
ENV DFG_PRODUCTION=True

CMD ["python3", "/dfg_server/cli/server.py"]
