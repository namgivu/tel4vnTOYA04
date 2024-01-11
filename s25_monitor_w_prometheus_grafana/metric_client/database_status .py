"""
cd $THIS_DIR

python -m pip install --upgrade pip virtualenv
python -m virtualenv venv

./venv/bin/python         -m pip install  prometheus-client psycopg2-binary
./venv/Scripts/python.exe -m pip install  prometheus-client psycopg2-binary
"""
from prometheus_client import start_http_server
import time

METRICS_INTERVAL=1

if __name__ == '__main__':
  start_http_server(8080) # start a prometheus metricclient; it's a httpserver app
  while True:
    # do_collect_some_metric()
    time.sleep(METRICS_INTERVAL)
