from unittest import TestCase


class TestSolution(TestCase):
    def test_solution(self):
        from build import solution

        dic = {'x': 500, 'y': 5874, 'z': 560}
        maxvalue = 5874
        minvalue = 500
        result = solution(dic)

        self.assertEqual(result[0], maxvalue)
        self.assertEqual(result[1], minvalue)

