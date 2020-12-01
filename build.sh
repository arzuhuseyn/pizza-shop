#!/usr/bin/env bash

# Any subsequent(*) commands which fail will cause the shell script to exit immediately
set -e

#Default values
CURRENT_PATH="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
ERROR_STATUS=0
VERSION="0.1"


# ------------------------
# Usage
function usage
{
  echo -e "Usage: $0 COMMAND"
  echo -e "\nCommands:"

  echo -e "\t setup  <- For setting up development environment"

  echo -en "\nPlease see the README file for more info.\n\n"
  exit 1
}


# ------------------------
# Setup development env
function setup() {
  #statements
  if which python3 > /dev/null 2>&1;
  then
    docker-compose \
			-f _development/docker-compose.yml \
		up --build -d
    #Python is installed
    python3 -m venv ${CURRENT_PATH}/.venv
    ${CURRENT_PATH}/.venv/bin/pip install -U pip
    ${CURRENT_PATH}/.venv/bin/pip install -r ${CURRENT_PATH}/requirements.txt
    source ${CURRENT_PATH}/.venv/bin/activate
    cd ${CURRENT_PATH}/app

    # Migrations
    python3 manage.py makemigrations
    python3 manage.py migrate
    
    # Start Server
    python3 manage.py runserver
  else
    # Python is not installed
    echo "We require python version >3"
  fi
}

################
#### START  ####
################

COMMAND=${@:$OPTIND:1}
ARGS=${@:$OPTIND:2}

#CHECKING PARAMS VALUES
case $COMMAND in
  setup)

    setup

    ;;

  *)

    if [[ $COMMAND != "" ]]; then
      echo "Error: Unknown command: $COMMAND"
      ERROR_STATUS=1
    fi
    usage

    ;;
esac

exit $ERROR_STATUS
