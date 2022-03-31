#!/bin/bash

pip install --upgrade pip
if [ "$MODE" = "development" ]; then
  pip install -r requirements/dev.txt
else
  pip install -r requirements/main.txt
fi