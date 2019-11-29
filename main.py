
from flask import Flask
import sys


app = Flask(__name__)


# [START app]
@app.route('/')
def hello_world():
    return 'Tranquility Base'
# [END app]


if __name__ == '__main__':
    app.run(debug=True)
