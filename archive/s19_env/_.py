secret_sai = 'viet oday la lo me no roi'

from pathlib import Path; SH=Path(__file__).parent
from dotenv import load_dotenv
load_dotenv(SH/'.env')

import os
secret = os.environ.get('MY_SECRET')
print(f'{secret=:>}')
