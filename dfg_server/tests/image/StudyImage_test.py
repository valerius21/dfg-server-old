import unittest

from dfg_server.db.db import DB
from dfg_server.image.StudyImage import StudyImage

db = DB()
img = StudyImage("tester", False, 1, db_client=db)


class MyTestCase(unittest.TestCase):
    def test_basic_image(self):
        self.assertIsNotNone(img.index)
        self.assertIsNotNone(img.is_private)
        self.assertIsNotNone(img.image_url)
        self.assertIsNotNone(img.uid)
        self.assertIsNotNone(img.db_client)

    def test_image_not_emtpy(self):
        self.assertNotEqual("", img.image_url)
        self.assertNotEqual("", img.uid)
        self.assertIsNotNone(img.image)
        self.assertTrue(1 <= img.index < 101)


if __name__ == '__main__':
    unittest.main()
