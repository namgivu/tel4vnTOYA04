"""
python -V
python -m pip install --upgrade pip virtualenv
python -m virtualenv venv

./venv/bin/python -m pip freeze
./venv/bin/python -m pip install flask requests pytest
./venv/bin/python -m pip freeze
# win /Scripts/python.exe
"""

from flask import Flask
import json

app = Flask(__name__)

@app.route('/')
def         index():
  return {}


@app.route('/github_latest_release')
def          github_latest_release():
  return {}


if __name__ == '__main__':
  #  .run                        host to run as dockercontainer lateron
  app.run(debug=True, port=5000, host='0.0.0.0')
  #  .run debug=True autoreload code if changed
