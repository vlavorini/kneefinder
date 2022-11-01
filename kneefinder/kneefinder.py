import matplotlib.pyplot as plt
from typing import Union
import numpy as np


class KneeFinder:
    """
    Knee point finder.

    This tool search for the point which has the maximum distance to a line
    passing for the fist and last point of the given data set.
    """
    knee = None

    def __init__(self, data_x: Union[list, np.ndarray], data_y: Union[list, np.ndarray, None] = None,
                 clean_data: bool = True):

        if isinstance(data_x, np.ndarray) and data_y is None:
            assert data_x.shape[0] == 2, "Unable to handle the data_x array"
            assert data_x.shape[1] > 2, "too few points to find a knee"

            self.data = data_x
            if clean_data:
                self.clean_data()
        else:
            assert len(data_x) == len(data_y), "data_x and data_x must have the same length"
            assert len(data_x) > 2
            # data ast two-dimensional array, for broadcasting
            self.data = np.vstack([data_x, data_y])
            if clean_data:
                self.clean_data()

        p1 = self.data.T[0]
        p2 = self.data.T[-1]

        # we need the line passing by the first and the last point
        p2mp1 = p2 - p1

        # adding an extra dimension for broadcasting
        self.p1 = np.expand_dims(p1, axis=1)
        self.p2mp1 = np.expand_dims(p2mp1, axis=1)

    def clean_data(self):
        # remove firsts and lasts equal values, if presents
        i_first = 0
        data_len = len(self.data[1])
        i_last = self.data[1][-1]
        first_value = self.data[1][0]
        last_value = self.data[1][-1]
        for i in range(data_len):
            if self.data[1][i] == first_value:
                i_first = i
            if self.data[1][data_len - i - 1] == last_value:
                i_last = i

        self.data = self.data[:, i_first:data_len - i_last]

    def find_knee(self) -> np.array:
        if self.knee is not None:
            return self.knee
        diff = self.p1 - self.data
        cross_prod = np.abs(np.cross(self.p2mp1, diff, axis=0))  # /norm(p2-p1) is useless in this context
        knee_position = np.argmax(cross_prod)
        self.knee = self.data[:, knee_position]
        return self.knee

    def plot(self, title: str = "Knee for this data") -> None:
        if self.knee is None:
            _ = self.find_knee()
        plt.plot(self.data[0], self.data[1], label="data")
        plt.plot([self.knee[0], self.knee[0]], [0, np.max(self.data[1])], '--', label=f"Knee at {self.knee}")
        plt.title(title)
        plt.legend()
        plt.show()
