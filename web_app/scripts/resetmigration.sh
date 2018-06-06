#!/bin/sh
alembic downgrade base
rm -rf migrations/versions/*
alembic revision --autogenerate -m "initial DB"
alembic upgrade head
python web_app/scripts/initialdata.py