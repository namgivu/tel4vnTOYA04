docstring="
access_token=xx ./composebuildup.sh
"

SH=$(cd `dirname ${BASH_SOURCE:-$0}` && pwd)
cd $SH

  access_token=${access_token}      \
  build_context="$SH/.."            \
  build_dockerfile="$SH/Dockerfile" \
    docker-compose build

  access_token=${access_token}      \
  build_context="$SH/.."            \
  build_dockerfile="$SH/Dockerfile" \
    docker-compose up
