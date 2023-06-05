#!/bin/sh

DRONE=false
NEIGE=false
MONT=false
quartier="Outremont"

while [ $# -gt 0 ]; do
    save=$#
    case $1 in
        -h|--help)
            cat README
            exit 1
            ;;
        -d|--drone)
            DRONE=true
            shift
            ;;
        -n|--deneigeuse)
            NEIGE=true
            shift
            ;;
        -m|--montreal)
            MONT=true
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
    if [ $# -ge $save ]; then
        echo Flag $1 invalide ou mal place.
        exit 1
    fi
done

if [


if [ DRONE ]; then
    echo -e CIRCUIT du drone arete par arete '\n' > data
    python3 drone/drone_quartier.py ${quartier} >> data

    if [ $? -eq 1 ]; then
        echo -e '\n=================================================='
        echo -e  ERROR: arrondissement ${quartier} inconnu essayer majuscule
        echo -e '==================================================\n'
        exit 1
    fi
    cat data
fi

if [ NEIGE ]; then
    echo -e 'phrase \n' > data
    python3 deneigement/cost.py ${quartier} >> data

    if [ $? -eq 1 ]; then
        echo -e '\n=================================================='
        echo -e  ERROR: arrondissement ${quartier} inconnu essayer majuscule
        echo -e '==================================================\n'
        exit 1
    fi
    cat data
fi
