#!/bin/sh

DRONE=false
MONT=false
COST=false
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
        -c|--cost)
            COST=true
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

if [ MONT ]; then
    if [ DRONE ]; then
        echo -e CIRCUIT du drone arete par arete '\n' > data
        echo -e CIRCUIT du drone arete par arete '\n'
        python3 drone/drone_montreal.py | tee -a data >> /dev/stdout
    fi
    if [ COST ]; then
        echo -e CIRCUIT du drone arete par arete '\n' > data
        echo -e CIRCUIT du drone arete par arete '\n'
        python3 cost/cost_montreal.py | tee -a data >> /dev/stdout
    fi
    exit 1
fi

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

if [ COST ]; then
    python3 cost/cost_quartier.py ${quartier} >> data
    cat data
fi
