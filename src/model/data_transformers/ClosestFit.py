from src.model.data_transformers.ReferenceFits import FitData


def find_O_fit(fit_data: FitData, raw_data: dict) -> str:
    """
    Calculate the least squares value between experimental data and the expected fitline
    :param fit_data: collection of all fit data
    :param raw_data: results from the end to end analysis
    """
    
    min_least_square = least_squares(fit_data.O_1, raw_data)
    return_str = "1"

    o_n_least_square = least_squares(fit_data.O_n, raw_data)
    if o_n_least_square <= min_least_square:
        min_least_square = o_n_least_square
        return_str = "n"

    o_logn_least_square = least_squares(fit_data.O_logn, raw_data)
    if o_logn_least_square <= min_least_square:
        min_least_square = o_logn_least_square
        return_str = "logn"

    o_n2_least_square = least_squares(fit_data.O_n2, raw_data)
    if o_n2_least_square <= min_least_square:
        min_least_square = o_n2_least_square
        return_str = "n2"

    o_n3_least_square = least_squares(fit_data.O_n3, raw_data)
    if o_n3_least_square <= min_least_square:
        min_least_square = o_n3_least_square
        return_str = "n3"

    o_nlogn_least_square = least_squares(fit_data.O_nlogn, raw_data)
    if o_nlogn_least_square <= min_least_square:
        min_least_square = o_nlogn_least_square
        return_str = "nlogn"

    o_nn_least_square = least_squares(fit_data.O_nn, raw_data)
    if o_nn_least_square <= min_least_square:
        min_least_square = o_nn_least_square
        return_str = "nn"

    o_nfact_least_square = least_squares(fit_data.O_n_fact, raw_data)
    if o_nfact_least_square <= min_least_square:
        min_least_square = o_nfact_least_square
        return_str = "n!"

    return return_str


def least_squares(fit_y, data_y) -> float:
    """
    Calculate the least squares value between experimental data and the expected fitline
    :param data_y: array of data from
    :param fit_y: results from the end to end analysis
    """

    # if len(data_y) != len(fit_y):
    #     raise RuntimeError("Fit data point count does not equal observed data point count.")
    ls_sum = 0.0
    for i in data_y:
        if fit_y[i] > 0:
            ls_sum += (data_y[i] - fit_y[i]) ** 2
        else:
            return 1.0e+20
        if ls_sum > 1.0e+20:
            break
    return round(ls_sum, 2)