#!/bin/bash
# Clemens Bauer
# Modified by Paul Bloom November 2022

# Serves nii volumes already on the computer's hard drive to MURFI (for simulating runs)


## ARGUMENTS ##

# TR (in ms)
tr=$4

# MNumber of volumes to serve
volumes=$3

# Path to directory with serve in simulation
path=$1

# File stem (an integer) indicating the number of the run that should be served
runstem=$2

if [ "$1" == "--help" ]; then
    echo "$0 [TR(ms)] [volumes] [path_spec]"
    exit 0
fi

port=15000
host='127.0.0.1' #localhost
sleep=1.2

echo $path

sleep $sleep
servepath=`which servenii`

if [ x"$servepath" == x ]; then
    echo "servenii not found, please add it to your path"
    #exit 1
fi


servenii ${path}img $runstem ${volumes} 1 68 $tr $port $host


