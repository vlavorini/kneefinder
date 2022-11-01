from unittest import TestCase
from ..kneefinder import KneeFinder


class TestCleanFlat(TestCase):
    """
    when the y's first points are the same, only the last is kept.

    Similar for the last points, where only the first is kept.
    """
    def test_first_two_same(self):
        # y of first two points is the same

        x = [1, 2, 3, 4, 5, 6]
        y = [10, 10, 9, 6, 3, 2]

        kf = KneeFinder(x, y)

        assert len(kf.data[1]) == len(y) - 1  # one point has been deleted

        # fisrt point deleted, second becomes the first
        assert kf.data[1][0] == y[1]
        assert kf.data[0][0] == x[1]

    def test_last_two_same(self):
        # y of last two points is the same
        x = [1, 2, 3, 4, 5, 6]
        y = [10, 9, 6, 3, 2, 2]

        kf = KneeFinder(x, y)

        assert len(kf.data[1]) == len(y) - 1  # one point has been deleted

        # last point deleted, second to last becomes the last
        assert kf.data[1][-1] == y[-2]
        assert kf.data[0][-1] == x[-2]

    def test_no_same(self):
        # y are all different
        x = [1, 2, 3, 4, 5, 6]
        y = [10, 9, 6, 3, 2, 1]

        kf = KneeFinder(x, y)
        assert len(kf.data[1]) == len(y)  # no deletion happened
