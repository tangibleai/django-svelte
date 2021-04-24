DATABASE_URL=sqlite3://db.sqlite3
export PYTHONPATH=$(dirname $(which python))
export PYTHON_PATH="$(pwd):$(dirname $PYTHONPATH)"
export DJANGO_SECRET_KEY=$(python -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())')
