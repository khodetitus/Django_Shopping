#!/bin/bash
#rm db.sqlite3
find . -path "*/migrations/*.py" -not -name "__init__.py" -delete -not -path "*/venv/*"