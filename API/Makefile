PROJECT_HOME=/home/dee/growow_backend/API
PYTHONPATH=${PROJECT_HOME}
DJANGO_SETTINGS_MODULE=
PYENV=${PROJECT_HOME}/pyenv
PYTHON=${PYENV}/bin/python
PYVIRTENVCMD=$(shell which virtualenv)
PIP=${PYENV}/bin/pip
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
		${PYTHON} ${PROJECT_HOME}/src/manage.py collectstatic --noinput ${SETTINGS}
	
db:
		${PYTHON} ${PROJECT_HOME}/src/manage.py makemigrations ${SETTINGS}
		${PYTHON} ${PROJECT_HOME}/src/manage.py migrate ${SETTINGS}


runserver:
		nohup ${PYTHON} ${PROJECT_HOME}/src/manage.py runserver ${LISTEN} ${SETTINGS} &


createsuperuser:
		${PYTHON} ${PROJECT_HOME}/src/manage.py createsuperuser ${SETTINGS}


migrations_init:
		${PYTHON} ${PROJECT_HOME}/src/manage.py makemigrations cc_core ${SETTINGS}
		${PYTHON} ${PROJECT_HOME}/src/manage.py makemigrations cc_dashboard ${SETTINGS}
		${PYTHON} ${PROJECT_HOME}/src/manage.py makemigrations cc_sshkeys ${SETTINGS}
		${PYTHON} ${PROJECT_HOME}/src/manage.py makemigrations cc_api ${SETTINGS}
		${PYTHON} ${PROJECT_HOME}/src/manage.py makemigrations cc_rdp ${SETTINGS}
		${PYTHON} ${PROJECT_HOME}/src/manage.py makemigrations cc_sip ${SETTINGS}


loaddata:
		${PYTHON} ${PROJECT_HOME}/src/manage.py loaddata ${SETTINGS} SSHKey 
		${PYTHON} ${PROJECT_HOME}/src/manage.py loaddata ${SETTINGS} SIPServer 
		${PYTHON} ${PROJECT_HOME}/src/manage.py loaddata ${SETTINGS} SIPClient
		${PYTHON} ${PROJECT_HOME}/src/manage.py loaddata ${SETTINGS} RDPServer 
		${PYTHON} ${PROJECT_HOME}/src/manage.py loaddata ${SETTINGS} CrShClient


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
		
		
		