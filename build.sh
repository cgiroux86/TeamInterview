#!/bin/bash
python3 manage.py db upgrade
gunicorn app main:app -w 2 --threads 2 -b 0.0.0.0:$PORT