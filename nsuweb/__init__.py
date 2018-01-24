from flask import Flask

app = Flask(__name__)

from nsuweb import routes
