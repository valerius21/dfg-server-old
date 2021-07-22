import unittest

from image.StudyImage import StudyImage

img = StudyImage("tester", False, 0)


class MyTestCase(unittest.TestCase):
    def test_basic_image(self):
        self.assertIsNotNone(img.index)
        self.assertIsNotNone(img.is_private)
        self.assertIsNotNone(img.imageURL)
        self.assertIsNotNone(img.uid)

    def test_image_not_emtpy(self):
        self.assertNotEqual("", img.imageURL)
        self.assertNotEqual("", img.uid)
        self.assertTrue(1 < img.index < 101)


if __name__ == '__main__':
    unittest.main()
