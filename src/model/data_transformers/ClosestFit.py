from src.model.data_transformers.ReferenceFits import FitData


def find_O_fit(fit_data: FitData, raw_data: dict) -> str:
    """
    Calculate the least squares value between experimental data and the expected fitline
    :param fit_data: collection of all fit data
    :param raw_data: results from the end to end analysis
    """
    if is_less_than_for_all_vals(fit_data.O_1, raw_data):
        return "1"

    if is_less_than_for_all_vals(fit_data.O_n, raw_data):
        return "n"

    if is_less_than_for_all_vals(fit_data.O_n, raw_data):
        return "n"

    if is_less_than_for_all_vals(fit_data.O_logn, raw_data):
        return "logn"

    if is_less_than_for_all_vals(fit_data.O_n2, raw_data):
        return "n2"

    if is_less_than_for_all_vals(fit_data.O_n3, raw_data):
        return "n3"

    if is_less_than_for_all_vals(fit_data.O_nlogn, raw_data):
        return "nlogn"

    if is_less_than_for_all_vals(fit_data.O_nn, raw_data):
        return "nn"

    if is_less_than_for_all_vals(fit_data.O_n_fact, raw_data):
        return "n!"

    return "1"


def is_less_than_for_all_vals(fit_y, data_y) -> bool:
    """
    Calculate the least squares value between experimental data and the expected fitline
    :param data_y: array of data from
    :param fit_y: results from the end to end analysis
    """

    for i in data_y.keys():
        if data_y[i] > fit_y[i]:
            return False

    return True
