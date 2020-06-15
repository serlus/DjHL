# DjHL
**Django Home Library** is a software that provides centralized management and process automation for the public,  private, school, and personal libraries, and offers features such as circulation, circulation history, administration,  cataloging, reporting, and patron records.

![CI](https://github.com/Riverfount/DjHL/workflows/CI/badge.svg)
[![Updates](https://pyup.io/repos/github/Riverfount/DjHL/shield.svg)](https://pyup.io/repos/github/Riverfount/DjHL/)
[![Python 3](https://pyup.io/repos/github/Riverfount/DjHL/python-3-shield.svg)](https://pyup.io/repos/github/Riverfount/DjHL/)

# How to Contribute

1. Clone the repository
1. Access the directory of your local repository
1. Install the project dependencies with Poetry
1. Copy the contrib/env-sample to .env
1. Change te value of SECRET_KEY with a valid Django secret key
1. If you want you can use the PostgreSQL change the DATABASE_URL with the correct parameters, but if you want to use the sqlite just comment this variable!
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
