import unittest
from unittest import TestCase

from bucket_list_app import app


class BucketListTest(TestCase):
    def setUp(self):
        # super(BucketListTest, self).setUp()
        # creates a test client
        self.app = app.test_client()
        # propagate the exceptions to the test client
        self.app.testing = True 

    def test_success(self):
        # sends HTTP GET request to the application
        # on the specified path
        result = self.app.get('/')
        self.assertEqual(result.status_code, 200)

if __name__ == '__main__':
    unittest.main()