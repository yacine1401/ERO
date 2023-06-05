#!/bin/sh

DRONE=false
TIEKS=false

while [ $# -gt 0 ]; do
    case $1 in
        -d|--drone)
            DRONE=true
            shift
            ;;
        -q|--quartier)
            TIEKS=true
            shift
            quartier=$1
            shift
            ;;
    esac
done

if [ TIEKS ]; then
    if [ quartier = "Outremont" ]


if [ DRONE ]; then

    echo -e CIRCUIT du drone arrete par arrete '\n' > data
    python3 parcours_drone/data_centering.py >> data
    cat data
fi
