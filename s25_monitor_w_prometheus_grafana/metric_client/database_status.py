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

#region define metric database_status
from prometheus_client import Gauge
METRIC_DEF = Gauge(
  name          = 'database_status',
  documentation = 'TOYA Demo @ Database Connection Status: 1 is ok, 0 is not ok',
  labelnames    = [ 'DB_HOST', 'DB_USERNAME', 'DB_DATABASE' ],
)
#endregion define metric database_status

if __name__ == '__main__':
  start_http_server(8080)  # start a prometheus metricclient; it's a httpserver app; aka 'prometheus metric-client httpserver' app
  while True:
    ##region collect metric database_status
    DB_HOST     = '0.0.0.0'
    DB_USERNAME = 'postgres'
    DB_PASSWORD = 'postgres'
    DB_DATABASE = 'postgres'

    new_metric_plot = METRIC_DEF.labels(DB_HOST, DB_USERNAME, DB_DATABASE) # new metric plot / new metric value

    try:
      #region ping :postgres
      conenction_string = f'host={DB_HOST} user={DB_USERNAME} password={DB_PASSWORD} dbname={DB_DATABASE}'
      import psycopg2
      conn = psycopg2.connect(conenction_string)
      cur = conn.cursor()
      cur.execute('SELECT 1')
      conn.close()
      #endregion ping :postgres

      # above postgres ping succeeded -> set database_status=1
      new_metric_plot.set(1)  # set metric value to 1

    except:
      # above postgres ping failed -> set database_status=0
      new_metric_plot.set(0)  # set metric value to 0
    ##endregion collect metric database_status

    time.sleep(METRICS_INTERVAL)
