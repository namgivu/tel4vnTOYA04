--- grafana --> prometheus
in ./grafana-provisioning/datasources/datasource.yml
  we have > url: http://prometheus:9090
this helps :grafana connect to :prometheus service

--- prometheus --> metric client as py code
in ./prometheus.yml
  we have > targets: ['host.docker.internal:8080']
this helps register our py :metricclient w/ :prometheus
