#!/bin/bash

echo $1 ' -> echo $1'

python manage.py dumpdata --indent=2  $1 > initial_data.json