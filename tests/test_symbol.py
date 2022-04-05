import os

from alphav import Symbol


def test_symbol():
    apikey = os.environ.get('API_KEY')
    s = Symbol('IBM', apikey)
    print(s.balance_sheet)
    print(s.earnings)
    print(s.income_statement)
    print(s.cash_flow)
    print(s.overview)
    print(s.global_quote)
    print(s.time_series_daily)
    print(s.time_series_monthly)
    print(s.time_series_monthly_adjusted)
    print(s.time_series_weekly)
    print(s.time_series_weekly_adjusted)
