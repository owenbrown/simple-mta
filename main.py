
# [START gae_python37_app]
import sys
import os

# Add vendor directory to module search path
parent_dir = os.path.abspath(os.path.dirname(__file__))
vendor_dir = os.path.join(parent_dir, 'lib')
sys.path.append(vendor_dir)

from flask import Flask  # noqa


app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Tranquility Base'
# [END app]


if __name__ == '__main__':
    app.run(debug=True)

# [END gae_python37_app]
