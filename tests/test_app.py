import unittest
from app import health_check

class TestHealthCheck(unittest.TestCase):

    def test_status(self):
        result = health_check()
        self.assertEqual(result["status"], "healthy")

    def test_service(self):
        result = health_check()
        self.assertEqual(result["service"], "devops-project")

    def test_environment(self):
        result = health_check()
        self.assertEqual(result["environment"], "development")

    def test_hostname(self):
        result = health_check()
        self.assertTrue(result["hostname"])

if __name__ == "__main__":
    unittest.main()



