import unittest

from dfg_server.image.handler import get_all_image_structs, _private_distribution

size = 100
half_size = int(size / 2)
uid = "tester"


class TestHandler(unittest.TestCase):
    def test_private_distribution_for_100(self):
        private = 0
        public = 0
        arr = _private_distribution(size)
        for e in arr:
            if e == 1:
                private += 1
            else:
                public += 1
        self.assertEqual(half_size, private)
        self.assertEqual(half_size, public)

    def test_get_all_image_structs_exists(self):
        arr = get_all_image_structs(uid)
        self.assertIsNotNone(arr)
        self.assertEqual(size, len(arr))

        for i in arr:
            self.assertEqual(uid, i.uid)

    def test_get_all_image_structs_for_non_accumulated_images(self):
        raise Exception("needs update")


if __name__ == '__main__':
    unittest.main()
