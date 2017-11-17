#!/bin/sh

# Migrate the database up
./bin/flask db upgrade

# Run gunicorn
gunicorn van_gogh.wsgi:app \
    -u nobody \
    --reload \
    --timeout=60 \
    --log-level=info \
    -b 0.0.0.0:8000

# Always smart to take a sec between restarts
sleep 1
