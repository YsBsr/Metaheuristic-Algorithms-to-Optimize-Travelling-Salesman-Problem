import numpy as np

class Coordinate:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    @staticmethod
    def get_distance(a, b):
        return np.sqrt(np.abs(a.x - b.x) + np.abs(a.y - b.y))

    @staticmethod # enerji fonksiyonu (uygunluk fonksiyonu)
    def get_total_distance(coordinates):
        dist = 0

        for first, second in zip(coordinates[:-1], coordinates[1:]):
            dist += Coordinate.get_distance(first, second)


        dist += Coordinate.get_distance(coordinates[0], coordinates[-1])

        return dist
