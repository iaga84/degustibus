#!/bin/bash

echo "Starting.."
python manage.py migrate --settings=degustibus.settings
python manage.py runserver 0.0.0.0:6969 --settings=degustibus.settings