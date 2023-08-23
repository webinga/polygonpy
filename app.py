from lightweight_charts import Chart
from datetime import date
from datetime import timedelta

yesterday = date.today() - timedelta(days=1)
if __name__ == "__main__":
    chart = Chart()
    chart.polygon.api_key("slItgdlk8bR20E2SnvItY_x7b7lXE0SB")
    chart.polygon.crypto(
        crypto_pair="BTC-USD",
        timeframe="1min",
        start_date=yesterday,
        end_date="now",
        limit=5000,
        live=True,
    )

    chart.show(block=True)
