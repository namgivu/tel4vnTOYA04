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
from prometheus_client import start_http_server


def get_folder_size(path):
  """disk usage in human readable format (e.g. '2,1GB') ref https://stackoverflow.com/a/25574638"""
  return subprocess.check_output(['du','-sh', path]).split()[0].decode('utf-8')

if __name__ == '__main__':
  # p='/var/lib/docker' ; print( f'{get_folder_size(p)} {p}' )
  # p='/var/cache'      ; print( f'{get_folder_size(p)} {p}' )

  start_http_server(8080)  # start a prometheus metricclient; it's a httpserver app; aka 'prometheus metric-client httpserver' app
