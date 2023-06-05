#!/bin/sh

DRONE=0
MONT=0
COST=0
TSP=0
quartier="Outremont"

while [ $# -gt 0 ]; do
    save=$#
    case $1 in
        -h|--help)
            cat README
            exit 1
            ;;
        -d|--drone)
            DRONE=1
            shift
            ;;
        -t|--tsp)
            TSP=1
            shift
            ;;
        -c|--cost)
            COST=1
            shift
            ;;
        -m|--montreal)
            MONT=1
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

if [ ${MONT} -eq 1 ]; then
    if [ ${DRONE} -eq 1 ]; then
        echo -e '================== DRONE: Montreal ================\n'
        echo -e CIRCUIT du drone arete par arete '\n'
        python3 drone/drone_montreal.py
    fi
    if [ ${COST} -eq 1 ]; then
        echo -e '\n================== COST: Montreal ================\n'
        python3 cost/cost_montreal.py
    fi
    if [ ${TSP} ]; then
        echo Pas de version montreal pour tsp
    fi
    exit 1
fi

if [ ${DRONE} -eq 1 ]; then
    echo -e '================== DRONE:' ${quartier} '================\n'
    python3 drone/drone_quartier.py ${quartier}

    if [ $? -eq 1 ]; then
        echo -e '\n=================================================='
        echo -e  ERROR: arrondissement ${quartier} inconnu essayer majuscule
        echo -e '==================================================\n'
        exit 1
    fi
    cat data
fi

if [ ${COST} -eq 1 ]; then
    echo -e '\n================== DRONE:' ${quartier} '================\n'
    python3 cost/cost_quartier.py ${quartier}
fi

if [ ${TSP} -eq 1 ]; then
    echo -e '\n================== TSP:' ${quartier} '================\n'
    python3 cost/tsp.py ${quartier}
fi
