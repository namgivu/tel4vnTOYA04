FROM python:3.11

WORKDIR /app

#                    WORKDIR
COPY ./src           ./src
COPY ./tests         ./tests
COPY ./zscript       ./zscript
#    context folder

RUN ls -lahF .

RUN python -m pip install --upgrade pip virtualenv
RUN python -m virtualenv ./venv
RUN                      ./venv/bin/python -m pip install flask requests pytest python-dotenv

CMD ./zscript/run.sh
