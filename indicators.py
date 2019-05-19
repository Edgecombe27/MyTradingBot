

# muiltiplier = 2 / (periods + 1)
# ema = (close - ema) * multiplier + ema
class EMA:

    # variables
    multiplier = 0
    periods = 0
    ema = 0
    count = 0

    # initializer
    def __init__(self, periods):
        self.multiplier = 2 / (periods + 1)
        self.periods = periods

    # methods
    def add(self, price):
        self.ema = (price - self.ema) * self.multiplier + self.ema
        self.count += 1

    def is_period_filled(self):
        return self.count >= self.periods


