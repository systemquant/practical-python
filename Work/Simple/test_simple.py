# test_simple.py

import simple
import unittest


class TestAdd(unittest.TestCase):
    def test_simple(self):
        # 단순한 정수 인자를 가지고 테스트
        r = simple.add(2, 2)
        self.assertEqual(r, 5)

    def test_str(self):
        r = simple.add('hello', 'world')
        self.assertEqual(r, 'helloworld')


unittest.main()
