
import sys
import os
os.getcwd()
sys.path.append(os.path.join(os.getcwd(), 'lib'))

from flask import Flask  # noqa


app = Flask(__name__)


# [START app]
@app.route('/')
def hello_world():
    return 'Tranquility Base'
# [END app]


if __name__ == '__main__':
    app.run(debug=True)
