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
    ##region collect metric database_status
    try:
      #region ping :postgres
      DB_HOST    ='0.0.0.0'
      DB_USERNAME='postgres'
      DB_PASSWORD='postgres'
      DB_DATABASE='postgres'

      conenction_string = f'host={DB_HOST} user={DB_USERNAME} password={DB_PASSWORD} dbname={DB_DATABASE}'
      import psycopg2
      conn = psycopg2.connect(conenction_string)
      cur = conn.cursor()
      cur.execute('SELECT 1')
      conn.close()
      #endregion ping :postgres

      # above postgres ping succeeded -> set database_status=1
      todo=122

    except:
      # above postgres ping failed -> set database_status=0
      todo=122
    ##endregion collect metric database_status

    time.sleep(METRICS_INTERVAL)
