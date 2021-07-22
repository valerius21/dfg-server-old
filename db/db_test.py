import unittest

from db import DB


class MyTestCase(unittest.TestCase):
    def test_not_none(self):
        db = DB()
        self.assertIsNotNone(db)
        self.assertIsNotNone(db.client)
        self.assertIsNotNone(db.transport)


if __name__ == '__main__':
    unittest.main()
