from flask import Flask

from urls import Urls
APP = Flask(__name__)
APP.env = 'development'
APP.testing = True
Urls.generate(APP)
if __name__ == '__main__':
    APP.run(debug=True)
