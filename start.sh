#!/bin/sh

# Run the Django development server
python manage.py runserver 0.0.0.0:8000 &

# Start the Tailwind process
python manage.py tailwind start
