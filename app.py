# -*- coding: utf-8 -*-
from flask import Flask
from GET.views import get_blueprint
from API.views import api_blueprint
from BOOKMARKS.views import bookmarks_blueprint


app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False

app.register_blueprint(get_blueprint)

app.register_blueprint(api_blueprint, url_prefix='/api')

app.register_blueprint(bookmarks_blueprint, url_prefix='/bookmarks')

app.run()
