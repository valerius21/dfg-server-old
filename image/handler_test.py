import unittest

from image.handler import add, private_distribution, get_all_image_structs

size = 100
half_size = int(size / 2)
uid = "tester"


class TestHandler(unittest.TestCase):

    def testing_test(self):
        self.assertEqual(5, add(2, 3))

    def test_private_distribution_for_100(self):
        private = 0
        public = 0
        arr = private_distribution(size)
        for e in arr:
            if e == 1:
                private += 1
            else:
                public += 1
        self.assertEqual(half_size, private)
        self.assertEqual(half_size, public)

    def test_get_all_image_structs(self):
        arr = get_all_image_structs(uid)
        self.assertIsNotNone(arr)
        self.assertEqual(size, len(arr))

        for i in arr:
            self.assertEqual(uid, i.uid)
            print(i)


if __name__ == '__main__':
    unittest.main()
