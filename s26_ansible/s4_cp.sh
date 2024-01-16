SH=$(cd `dirname $BASH_SOURCE` && pwd)
ansible  -i "$SH/hosts" 'all'  -m ansible.builtin.'copy' -a "src=./hosts dest=/tmp/hosts"
