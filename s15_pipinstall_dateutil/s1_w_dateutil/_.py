import dateutil

#region intro .venv/bin/python to pip install :package

# cd :thisdir
# python _.py
# error > ModuleNotFoundError: No module named 'dateutil'

# python -m pip freeze
'''
python -m pip freeze
astunparse==1.6.3
certifi==2023.11.17
chardet==5.2.0
distlib==0.3.7
filelock==3.13.1
pipenv==2023.11.15
platformdirs==4.1.0
pyflowchart==0.3.1
six==1.16.0
virtualenv==20.25.0
'''

# ./.venv/bin/python -m pip freeze
'''
(empty)
'''

# ./.venv/bin/python -m pip install --upgrade pip dateutils
# ./.venv/bin/python -m pip freeze  #NOTE it is completely different w/ system python ie > python -m pip freeze
'''
dateutils==0.6.12
python-dateutil==2.8.2
pytz==2023.3.post1
six==1.16.0
'''

# ./.venv/bin/python _.py
# (now no error )

#endregion intro .venv/bin/python to pip install :package


###

'''Con baonhieu ngay nua thi den Tet? '''
'''Con baonhieu gio  nua thi den Tet? '''

'''
Tet batdau tu 28/12 amlich
2023 thi ngay nay la ngay 2024-02-07
'''
from datetime import datetime
# tet_d = datetime('2024-02-07')  # error w/ builtin datetime package
tet_d = datetime(2024, 2, 7)
tet_d = datetime.strptime('2024-02-07', '%Y-%m-%d')

# dateutil comes in handy - convert human-friendly date into python datetime object
from dateutil import parser
tet_d = parser.parse('2024-02-07')
print(tet_d)

today_d = datetime.today()
print(     tet_d-today_d )  # in days
print( f'{(tet_d-today_d).total_seconds() * 3600} hours' )  # in hours  ref ggbard https://g.co/bard/share/b0a4dfe0c300
