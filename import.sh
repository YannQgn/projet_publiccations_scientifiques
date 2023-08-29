#!/bin/bash

# Importer les données avec mongoimport
mongoimport --db DBLP --collection publis --file /dblp.json --username root --password example --host mongodb --port 27017

# Attendre indéfiniment
while true; do
  sleep 3600  # Attendre 1 heure avant de vérifier à nouveau
done
