SH=$(cd `dirname $BASH_SOURCE` && pwd)
ansible  -i "$SH/hosts" 'all'  -m ping
