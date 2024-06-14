#!python

try:
    from dotenv import set_key, load_dotenv
except Exception:
    print("DOTENV MISSING RUN:")
    print("pip install python-dotenv==0.21.1")
    exit()

import os

# CHECK DIRECTORY
current_dir = os.getcwd()
script_file = os.path.abspath(__file__)
if not(current_dir == os.path.dirname(script_file)):
    print("PLEASE RUN CONFIG SCRIPT INSIDE PROJECT DIRECTORY")
    exit()

load_dotenv()  # Carga el archivo .env automáticamente

project = os.getenv('PROJECT')
odoo_version = os.getenv('ODOO_VERSION')
port = os.getenv('PORT')
db_password = os.getenv('DB_PASSWORD')

env_variables = [
    {'prompt': 'Project (lowercase)', 'value': project, 'name': 'PROJECT'},
    {'prompt': 'Odoo Version', 'value': odoo_version, 'name': 'ODOO_VERSION'},
    {'prompt': 'Port', 'value': port, 'name': 'PORT'},
    {'prompt': 'DB Password', 'value': db_password, 'name': 'DB_PASSWORD'}
]

env_values = {}
for variable in env_variables:
    if variable['value']:
        value = input(variable['prompt'] + ' [%s]: ' % variable['value'])
        if not value:
            value = variable['value']
    else:
        value = input(variable['prompt'] + ': ')
        while not value:
            value = input(variable['prompt'] + ': ')
    env_values[variable['name']] = value

# WRITE ENV FILE
env_file_path = '.env'
for key, value in env_values.items():
    set_key(env_file_path, key, value)
