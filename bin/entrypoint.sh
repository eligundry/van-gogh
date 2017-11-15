#!/bin/sh

# Run gunicorn
gunicorn -u nobody app.wsgi:app --reload --timeout=60 --log-level=info

# Always smart to take a sec between restarts
sleep 1
