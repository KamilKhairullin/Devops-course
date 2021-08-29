
import requests
import pytest
import unittest

@pytest.fixture
def client():
    pass

def test_acess(client):
    r = requests.get("http://127.0.0.1:5000")
    assert r.status_code == 200, "Unreached."


# class FlaskrTestCase(unittest.TestCase):
#     def setUp(self):
#         pass
#     def tearDown(self):
#         pass

#     def request_test(self):
#         #r = requests.get("http://127.0.0.1:5000")
#         assert False#r.status_code == 200, "Unreached."

# #if __name__ == '__main__':
# unittest.main()
