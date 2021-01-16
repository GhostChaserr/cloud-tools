#!/bin/sh
export LC_ALL=C.UTF-8 && export LANG=C.UTF-8 
export APP_NAME="CLOUD TOOLS API!"

uvicorn app:app --host 0.0.0.0 --port 5200 --workers=3 --reload