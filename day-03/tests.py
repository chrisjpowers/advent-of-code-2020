from unittest import TestCase
from a import Hill, Sled

TEST_HILL = """..##.......
#...#...#..
.#....#..#.
..#.#...#.#
.#...##..#.
..#.##.....
.#.#.#....#
.#........#
#.##...#...
#...##....#
.#..#...#.#""".split("\n")


class TestA(TestCase):
    def setUp(self):
        self.hill = Hill.parse(TEST_HILL)

    def test_hill(self):
        self.assertEqual(self.hill.width, 11)
        self.assertEqual(self.hill.height, 11)
    
    def test_sled(self):
        sled = Sled(self.hill, (3,1))
        sled.run()
        self.assertEqual(sled.trees, 7)
