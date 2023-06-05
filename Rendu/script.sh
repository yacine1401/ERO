#!/bin/sh

DRONE=false
quartier="Outremont"

while [ $# -gt 0 ]; do
    case $1 in
        -d|--drone)
            DRONE=true
            shift
            ;;
        -q|--quartier)
            shift
            if [ $# -le 0 ]; then
                echo Nom d\'arrondissement attendu apres -q ou --quartier
                exit 1
            fi
            quartier=$1
            shift
            ;;
    esac
done

if [ DRONE ]; then
    echo -e CIRCUIT du drone arrete par arrete '\n' > data
    python3 parcours_drone/data_centering.py ${quartier} >> data

    if [ $? -eq 1 ]; then
        echo -e '\n' =====================
        echo -e  ERROR: arrondissement ${quartier} inconnu essayer majuscule
        echo -e ====================== '\n'
        exit 1
    fi
    cat data
fi
