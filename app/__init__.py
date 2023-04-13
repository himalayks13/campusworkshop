"""Setup at app startup"""
from flask import Flask
import psycopg2


app = Flask(__name__)
postgres = psycopg2.connect(
        host="dpg-cgrq3mfdvk4rjsv9fmqg-a.oregon-postgres.render.com",
        database="test_nknk",
        user="test_nknk_user",
        password="A3npAxHOlsTg2esiCIibJAbABMpOBxDx")
# To prevent from using a blueprint, we use a cyclic import
# This also means that we need to place this import here
# pylint: disable=cyclic-import, wrong-import-position
from app import routes
