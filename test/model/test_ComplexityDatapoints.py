import math

from src.model.ComplexityDatapoints import get_o_1_data, get_o_n_data, get_o_n2_data


def test_get_o_1_data():
    x_values = [0, 1, 10, 15, 34]
    y_values = [5, 6, 7, 8, 9]
    o_1_fit = get_o_1_data(x_values, y_values)

    for x in x_values:
        assert o_1_fit[x] == 5


def test_get_o_n_data():
    x_values = [0, 1, 2, 3, 4, 6]
    y_values = [5, 6, 7, 8, 9, 11]
    o_n_fit = get_o_n_data(x_values, y_values)

    tolerance = 0.001
    for x in range(0, 7):
        assert x + 5 - tolerance <= o_n_fit[x] <= x + 5 + tolerance


def test_get_o_n2_data():
    x_values = [0, 1, 2, 3, 4, 6, 7, 8, 9, 10]
    y_values = [4, 4.9, 9.2, 13, 20, 40, 53, 68, 85, 104]
    o_n_fit = get_o_n2_data(x_values, y_values)

    tolerance = 0.3
    for x in range(0, 7):
        assert math.pow(x, 2) + 4 - tolerance <= o_n_fit[x] <= math.pow(x, 2) + 4 + tolerance
