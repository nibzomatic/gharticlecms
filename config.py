import os
from urllib.parse import quote_plus

basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'secret-key'

    SQL_SERVER = os.environ.get('SQL_SERVER') or 'ssarticlecms3.database.windows.net'
    SQL_DATABASE = os.environ.get('SQL_DATABASE') or 'dbArticleCMS3'
    SQL_USER_NAME = os.environ.get('SQL_USER_NAME') or 'cmsadmin3'
    SQL_PASSWORD = os.environ.get('SQL_PASSWORD') or 'F@ncyP@ssw0rd3'
    ENCODED_PASSWORD = quote_plus(SQL_PASSWORD)

    # Below URI may need some adjustments for driver version, based on your OS, if running locally
    SQLALCHEMY_DATABASE_URI = 'mssql+pyodbc://' + SQL_USER_NAME + '@' + SQL_SERVER + ':' + ENCODED_PASSWORD + '@' + SQL_SERVER + ':1433/' + SQL_DATABASE  + '?driver=ODBC+Driver+17+for+SQL+Server&timeout=30'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    BLOB_ACCOUNT = os.environ.get('BLOB_ACCOUNT') or 'saarticlecms'
    BLOB_STORAGE_KEY = os.environ.get('BLOB_STORAGE_KEY') or 'wdPA1JVuGFcZHYlSnqu5PMRBJKjXKQB0ta+zC5THd/yCUYmG6vfmoSvv5W2/nNjUIHwZ/amFhE3L+ASt4tPIiw=='
    BLOB_CONTAINER = os.environ.get('BLOB_CONTAINER') or 'scimages'

    ### Info for MS Authentication ###
    ### As adapted from: https://github.com/Azure-Samples/ms-identity-python-webapp ###
    CLIENT_SECRET = "E348Q~V2Z0kEd~OY29qeIySh3_aLrPPH2_Dlqbg_"
    # In your production app, Microsoft recommends you to use other ways to store your secret,
    # such as KeyVault, or environment variable as described in Flask's documentation here:
    # https://flask.palletsprojects.com/en/1.1.x/config/#configuring-from-environment-variables
    # CLIENT_SECRET = os.getenv("CLIENT_SECRET")
    # if not CLIENT_SECRET:
    #     raise ValueError("Need to define CLIENT_SECRET environment variable")

    AUTHORITY = "https://login.microsoftonline.com/common"  # For multi-tenant app, else put tenant name
    # AUTHORITY = "https://login.microsoftonline.com/Enter_the_Tenant_Name_Here"

    CLIENT_ID = "d2b06aef-b2fa-4d5e-9e95-5434d6dd9935"


    REDIRECT_PATH = "/getAToken"  # Used to form an absolute URL; must match to app's redirect_uri set in AAD

    # You can find the proper permission names from this document
    # https://docs.microsoft.com/en-us/graph/permissions-reference
    SCOPE = ["User.Read"] # Only need to read user profile for this app

    SESSION_TYPE = "filesystem"  # Token cache will be stored in server-side session