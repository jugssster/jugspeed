#!/bin/bash
Welcome () {
  echo "*%* Jugspeed CONTROL PANEL *%*"
  echo " 0 - initialize"
  echo "   Options: [ debug ] , [ --env <file path> ]"
  echo "   Usage: $ ./cms.sh debug --env /home/User/.env"
  echo " 1 - rebuild app"
  echo " 2 - backup"
  echo " 3 - restore"
  exit
}

Wait () {
  sec=5
  while [ $sec -ne 0 ]; do
    if [ $DEBUG_MODE != True ]; then
      clear
    fi
    echo "Wait to start in $sec second..."
    sleep 1
    ((sec=sec-1))
  done
}

CheckEnv () {
  # check env file existance
  if [ -f .env ]; then
    # set default
    DEBUG_MODE=False
    if [ "$1" == "debug" ]; then
      # update debug mode
      DEBUG_MODE=True
    fi
    # update .env file
    sed -i "s/DEBUG_MODE=False/DEBUG_MODE=$DEBUG_MODE/" .env
    sed -i "s/DEBUG_MODE=True/DEBUG_MODE=$DEBUG_MODE/" .env
    # export all variables
    export $(grep -v '^#' .env | xargs -0)
    echo "environment file is OK."
  else
    echo "environment file DOES NOT FOUND."
    exit
  fi
}

case $1 in
  0)
    CheckEnv "$2"
    printf "THIS ACTION WILL REMOVE DATABASE! Do you have backups? [yes]:"
    read confirm
    if [ $confirm != yes ]; then
      echo "Operation aborted."
     exit
    fi
    docker-compose down -v -t 0
    if [ $DEBUG_MODE == True ]; then
      docker-compose build
    else
      docker-compose build --force-rm --no-cache
    fi
    docker-compose up -d
    if [ $? -ne 0 ]; then
      echo "Could not init Jugspeed, Check log above."
      exit
    fi
    Wait
    printf "\nJugspeed is Running!"
    ;;

  1)
    docker container restart -t 0 jugspeed_App
    if [ $? -ne 0 ]; then
      echo "Could not rebuild App, Check log above."
      exit
    fi
    echo "App successfully rebuilt."
    ;;

  *)
    Welcome
    ;;

esac