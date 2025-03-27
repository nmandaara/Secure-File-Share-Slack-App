#!/bin/bash


echo "Installing requirements..." | tee -a log_startup.log
pip install -r requirements.txt >> log_startup.log 2>&1
if [ $? -ne 0 ]; then
    echo "pip install failed" | tee -a log_startup.log
    exit 1
fi

cd /home/site/wwwroot || exit 1

echo "Running credential test..." | tee -a log_startup.log
python3 test_credential.py >> log_startup.log 2>&1

echo "Starting gunicorn..." | tee -a log_startup.log
gunicorn --bind=0.0.0.0:8000 app:app >> log_startup.log 2>&1
if [ $? -ne 0 ]; then
    echo "gunicorn failed to start" | tee -a log_startup.log
    exit 1
fi

echo "Gunicorn exited" | tee -a log_startup.log