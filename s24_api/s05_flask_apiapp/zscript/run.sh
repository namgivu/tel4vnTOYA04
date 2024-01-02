SH=$(cd `dirname ${BASH_SOURCE:-$0}` && pwd)
AH=`cd "$SH/.." && pwd`

PYTHONPATH=$AH "$AH/venv/bin/python" "$AH/src/flask_apiapp.py"
