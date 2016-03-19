PROJECT_HOME=/home/dee/growow_backend/API
PYTHONPATH=${PROJECT_HOME}
DJANGO_SETTINGS_MODULE=
PYENV=${PROJECT_HOME}/pyenv
PYTHON=${PYENV}/bin/python
PYVIRTENVCMD=$(shell which virtualenv)
PIP=${PYENV}/bin/pip
DJANGO_MANAGE=${PROJECT_HOME}/apiwebapp/manage.py
SETTINGS= 
# --settings=${DJANGO_SETTINGS_MODULE}
#LISTEN=127.0.0.1:8064
LISTEN=0.0.0.0:8064
TARGET_OS=$(shell uname -s)



all: up db collectstatic stop.sh
		git status

up:
		git pull

collectstatic:
		${PYTHON} ${DJANGO_MANAGE} collectstatic --noinput ${SETTINGS}
	
db:
		${PYTHON} ${DJANGO_MANAGE} makemigrations ${SETTINGS}
		${PYTHON} ${DJANGO_MANAGE} migrate ${SETTINGS}


runserver:
		nohup ${PYTHON} ${DJANGO_MANAGE} runserver ${LISTEN} ${SETTINGS} &


createsuperuser:
		${PYTHON} ${DJANGO_MANAGE} createsuperuser ${SETTINGS}


env: ${PYTHON}
		${PIP} install -r pip.freeze.${TARGET_OS}


${PYTHON}: ${PYVIRTENVCMD} ${TARGET_OS}
		virtualenv ${PYENV}


/usr/bin/virtualenv:
		sudo apt-get -y install python-virtualenv python-dev


Linux:
		sudo apt-get -y install mysql-server libmysqlclient-dev python-dev
		

FreeBSD:
		echo "Not implemented" 
		exit 127


stop.sh: 
		echo "ps axwwwww | grep ${LISTEN} | grep -v grep | awk '{ print "'$$1'" }' | xargs kill" > stop.sh
		chmod +x ./stop.sh


		
