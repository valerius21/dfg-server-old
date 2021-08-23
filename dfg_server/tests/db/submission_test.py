import unittest

from dfg_server.db.submission import Submission, SubmissionContradictionError

everything_false_data = {
    'sensitivity': '2',
    'is_private': True,
    'photo_id': 1337,
    'uid': 'tester',
    'acquaintance': False,
    'colleagues': False,
    'family': False,
    'friends': False,
    'everybody': False,
    'nobody': False,
}

everything_true_data = {
    'sensitivity': '2',
    'is_private': True,
    'photo_id': 1337,
    'uid': 'tester',
    'acquaintance': True,
    'colleagues': True,
    'family': True,
    'friends': True,
    'everybody': True,
    'nobody': True,
}

any_except_everybody_and_nobody_data = {
    'sensitivity': '2',
    'is_private': True,
    'photo_id': 1337,
    'uid': 'tester',
    'acquaintance': False,
    'colleagues': True,
    'family': False,
    'friends': False,
    'everybody': False,
    'nobody': False,
}

everybody_and_nobody_data = {
    'sensitivity': '2',
    'is_private': True,
    'photo_id': 1337,
    'uid': 'tester',
    'acquaintance': False,
    'colleagues': False,
    'family': False,
    'friends': False,
    'everybody': True,
    'nobody': True,
}

nobody_and_any_data = {
    'sensitivity': '2',
    'is_private': True,
    'photo_id': 1337,
    'uid': 'tester',
    'acquaintance': False,
    'colleagues': False,
    'family': True,
    'friends': False,
    'everybody': False,
    'nobody': True,
}

everything_false = Submission(**everything_false_data)
everything_true = Submission(**everything_true_data)
any_except_everybody_and_nobody = Submission(**any_except_everybody_and_nobody_data)
everybody_and_nobody = Submission(**everybody_and_nobody_data)
nobody_and_any = Submission(**nobody_and_any_data)


class SubmissionTest(unittest.TestCase):
    def setUp(self) -> None:
        self.submissions = []
        for i in range(64):
            target_demography = bin(i)[2:]
            target_demography = '{:0>6}'.format(target_demography)
            target_demography = [c == '1' for c in target_demography]
            test_submission_data = {
                'sensitivity': '2',
                'is_private': True,
                'photo_id': 1337,
                'uid': 'tester',
                'acquaintance': target_demography[0],
                'colleagues': target_demography[1],
                'family': target_demography[2],
                'friends': target_demography[3],
                'everybody': target_demography[4],
                'nobody': target_demography[5],
            }
            self.submissions.append(Submission(**test_submission_data))

    def tearDown(self) -> None:
        self.submissions = []

    def test_everything_true_throws_error(self):
        with self.assertRaises(SubmissionContradictionError):
            everything_false.check()
            [s.check() for s in self.submissions]

    def test_everything_false_throws_error(self):
        with self.assertRaises(SubmissionContradictionError):
            everything_true.check()
            [s.check() for s in self.submissions]

    def test_any_except_everybody_and_nobody(self):
        self.assertTrue(
            any(
                any_except_everybody_and_nobody.check()[:-2]
            )
        )

    def test_everybody_and_nobody(self):
        with self.assertRaises(SubmissionContradictionError):
            everybody_and_nobody.check()
            [s.check() for s in self.submissions]

    def test_nobody_and_anything(self):
        with self.assertRaises(SubmissionContradictionError):
            nobody_and_any.check()
            [s.check() for s in self.submissions]


if __name__ == '__main__':
    unittest.main()
