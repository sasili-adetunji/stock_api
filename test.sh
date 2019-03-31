#!/bin/bash

env=$1
file=""

if [[ "${env}" == "dev" ]]; then
  file="docker-compose-dev.yml"
elif [[ "${env}" == "prod" ]]; then
  file="docker-compose-prod.yml"
else
  echo "USAGE: ./test.sh environment_name"
  echo "* environment_name: must either be 'dev', or 'prod'"
  exit 1
fi


/bin/sleep 3

docker-compose -f $file run users python manage.py test

docker-compose -f $file run stocks python manage.py test

echo "All Tests passed!"
exit 0