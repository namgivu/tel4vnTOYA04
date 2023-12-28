import os
secret = os.environ.get('MY_SECRET')
print(f'secret={secret if secret else ""}')
