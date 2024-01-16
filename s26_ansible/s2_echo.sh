SH=$(cd `dirname $BASH_SOURCE` && pwd)
ansible  -i "$SH/hosts" 'all'  -a '/bin/echo "abb 122" '
