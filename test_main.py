import main
import unittest

import sys
print(sys.version)


class MainTest(unittest.TestCase):

    def setUp(self):
        self.app = main.app.test_client()

    def test_hello_world(self):
        encoding = 'utf-8'
        rv = self.app.get('/')
        s = rv.data.decode(encoding)
        assert s == 'Tranquility Base'


if __name__ == '__main__':
    unittest.main()


