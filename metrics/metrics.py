import numpy as np


def get_metrics(data):
    all_rates = data['rates']
    dates = list(all_rates.keys())
    print(dates)

    currencies = list(all_rates[dates[0]])
    print(currencies)

    # dictionary (currency -> rates over all period)
    currency_rates = {currency: [] for currency in currencies}

    for date in dates:
        rates_at_date = all_rates[date]
        for currency in rates_at_date:
            currency_rates[currency].append(rates_at_date[currency])

    result = dict()

    for currency in currencies:
        std_dev = np.std(currency_rates[currency])
        avg = np.average(currency_rates[currency])
        var = np.var(currency_rates[currency])
        result[currency] = {'std_dev': std_dev, 'avg': avg, 'var': var}

    return result
