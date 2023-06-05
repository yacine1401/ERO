#!/bin/sh

Drone=false

while [ $# -gt 0 ]; do
    case $1 in
        -d|--drone)
            Drone=true
            shift
            ;;
    esac
done

if [ Drone ]; then
    echo -e CIRCUIT du drone arrete par arrete '\n' > data
    python3 center.py >> data
    cat data
fi
