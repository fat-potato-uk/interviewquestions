#!/bin/bash

# This script should be run from inside a docker ubuntu image
# to start a docker image use the command:
# docker run -it --rm --entrypoint /bin/bash -v $(pwd):/code:ro ubuntu:latest
# Then run /code/build.sh inside the container

if [ ! -r /etc/lsb-release ] ; then
    echo "Unable to find the OS release file, please run inside an Ubuntu container" >&2
    exit 1
fi

apt update
apt install -y build-essential cmake
mkdir /build
cd /build
cmake ../code
make && /build/tests/unit_tests
