"""
company project use docker image to run on gcp cloudrun
image built from a computeengine server --> docker cache keep growing big thru time
eg after 3 months, it grows to 60Gb --> making the server stop working --> need a docker cache clean/prune

in short, need a monitor of docker cache 's occupied disk size
ie monitor a folder size

DONE get foldersize fr forlder_path  ref https://stackoverflow.com/a/25574638
DONE send foldersize plot to prometheus --> later have grafana draw it
"""
import subprocess
#
from prometheus_client import start_http_server, Gauge
import time


def get_folder_size(path):
  """disk usage in human readable format (e.g. '2,1GB') ref https://stackoverflow.com/a/25574638"""
  # return subprocess.check_output(['du','-sh', path]).split()[0].decode('utf-8')
  return   subprocess.check_output(['du','-s',  path]).split()[0].decode('utf-8')

if __name__ == '__main__':
  # p='/var/lib/docker' ; print( f'{get_folder_size(p)} {p}' )
  # p='/var/cache'      ; print( f'{get_folder_size(p)} {p}' )

  start_http_server(8080)  # start a prometheus metricclient; it's a httpserver app; aka 'prometheus metric-client httpserver' app
  metric_define_obj = Gauge(
    name          = 'folder_size',
    documentation = 'toya demo folder_size',
    labelnames    = [ 'path' ],
  )
  while True:
    ##region get foldersize as new metric plot and print to :8080 stream
    path = '/var/lib/docker'

    # prepare prometheusclient plot obj
    new_metric_plot = metric_define_obj.labels(path)

    # print(sz)  # we want this print to print to :prometheus scrapejob --> print into :8080 stream --> need new prometheusclient plot obj aka :new_metric_plot
    sz = get_folder_size(path)
    new_metric_plot.set(sz)

    #region 2nd line of same metric
    '''view sample 
    1line metric_1line.gif
    3line metric_3line.png
    '''
    path2 = '/var/cache'
    new_metric_plot2 = metric_define_obj.labels(path2)
    new_metric_plot2.set( get_folder_size(path2) )
    #endregion 2nd line of same metric

    ##endregion get foldersize as new metric plot and print to :8080 stream

    time.sleep(3)
