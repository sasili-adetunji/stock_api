#! /bin/bash


function build_up() {
    printf "***************************************************\n    Building the image \n***************************************************\n"
    # Install required packages

    echo "======= Making entrypoint executable ========"
    chmod +x services/users/entrypoint.sh
    chmod +x services/stocks/entrypoint.sh

    echo "======= Building up with docker-compose ========"
    docker-compose -f docker-compose-dev.yml up -d --build

}
######################################################################
########################      RUNTIME       ##########################
######################################################################

build_up
