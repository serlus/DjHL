# DjHL
**Django Home Library** is a software that provides centralized management and process automation for the public,  private, 
school, and personal libraries, and offers features such as circulation, circulation history, administration,  cataloging,
reporting, and patron records.

![CI](https://github.com/Riverfount/DjHL/workflows/CI/badge.svg)
[![Updates](https://pyup.io/repos/github/Riverfount/DjHL/shield.svg)](https://pyup.io/repos/github/Riverfount/DjHL/)
[![Python 3](https://pyup.io/repos/github/Riverfount/DjHL/python-3-shield.svg)](https://pyup.io/repos/github/Riverfount/DjHL/)

# How to Contribute

We use [Poetry](https://python-poetry.org) to manage our virtualenv and dependencies. If you don't use the poetry don't 
forget to install the dev dependencies. You can know what are the dev dependencies into pyproject.toml file.

1. Clone the repository
1. Access the directory of your local repository
1. Install the project dependencies with Poetry
1. Copy the contrib/env-sample to .env
1. Change te value of SECRET_KEY with a valid Django secret key
1. If you want, you can use PostgreSQL in docker, for that just use the Docker-compose file present in 
the project, but if you want to use sqlite, just comment this variable!
1. After the BD set up run the Django Migrations

These steps in code:

```bash
git clone git@github.com:Riverfount/DjHL.git
cd DjHL
poetry install
cp contrib/env-sample .env
# Open the .env with your editor and change the variables SECRET_KEY and DATABASE_URL
python manage.py migrate
```

#### To generate a SECRET_KEY for your Django Project you can do:

##### Poetry

Using Poetry, in the directory of the project execute this command to enter at python console:

```bash
poety run python
```

In the console python you can execute these commands to get a SECRET_KEY value:

```python
from django.core.management.utils import get_random_secret_key

print(get_random_secret_key())
```

##### Linux and similars

In the project's directory you need to activate the virtualenv and run the console python and, after that execute the 
same commands above.

To activate the virtualenv if your virtualenv was installed in the .venv direcotry execute the following command:

```bash
source .venv/bin/activate
``` 

##### Windows

You need to entar at CMD and go to the project's directory and activate the virtualenv and run the console python and, 
after that execute the same commands above.

To activate the virtualenv if your virtualenv was installed in the .venv direcotry execute the following command:

```cmd
.venv/Scripts/activate
```

##### Running the database in docker

***Prerequisites:***
 - Docker
 - Docker-Compose
 
1. To run the database, simply run the following command.

```console
docker-compose -f Docker-compose up -d
```
1. To stop the database, just run the following command
```console
docker-compose -f Docker-compose stop
```

#### ***For the installation of the prerequisites see:***
- [Docker install](https://docs.docker.com/engine/install/)
- [Docker-Compose install](https://docs.docker.com/compose/install/)