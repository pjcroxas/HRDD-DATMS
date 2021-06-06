#!/bin/bash

gunicorn --bind 0.0.0.0:8000 OTMS.wsgi --log-level info  --access-logfile logs/OTMS-access.log --error-logfile logs/OTMS-error.log  &
