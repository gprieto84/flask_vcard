import urllib
import os

class Config(object):   
    # Build the MSSQL ULR for SqlAlchemy
    params = urllib.parse.quote_plus('DRIVER={SQL Server};SERVER=Cobartram016\TRABDSP10;DATABASE=BDVIAJE2;UID=tra-pbi;PWD=12345.PBI;')
    mssql_url = "mssql+pyodbc:///?odbc_connect=%s" % params

    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    SQLALCHEMY_DATABASE_URI = mssql_url
    SQLALCHEMY_TRACK_MODIFICATIONS = False


