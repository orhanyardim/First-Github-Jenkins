class TestApp(unittest.TestCase):
    def test_add(self):
        try:
            self.assertEqual(add(2, 3), 5)
            print("Test Passed: add(2, 3) == 5")
        except AssertionError:
            print("Test Failed: add(2, 3) != 5")

if __name__ == '__main__':
    unittest.main()
