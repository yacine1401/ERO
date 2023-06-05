#!/bin/sh

DRONE=false
NEIGE=false
quartier="Outremont"

while [ $# -gt 0 ]; do
    case $1 in
        -d|--drone)
            DRONE=true
            shift
            ;;
        -n|--deneigeuse)
            NEIGE=true
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
    echo -e CIRCUIT du drone arete par arete '\n' > data
    python3 parcours_drone/data_centering.py ${quartier} >> data

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
