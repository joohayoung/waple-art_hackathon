from statsmodels.tsa.arima_model import ARIMA
import statsmodels.api as sm
import numpy as np

def make_arima(data, order):

    model = ARIMA(data, order = order)
    model_fit = model.fit(trend="nc", full_output=True, dips=1)

    return model_fit

def pred_data(model_fit, steps):

    fore = model_fit.forecast(steps=steps)

    return np.round(fore[0])