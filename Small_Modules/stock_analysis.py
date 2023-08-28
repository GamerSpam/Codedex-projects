# Stoncks lesson from Codedex

stock_prices = [ 6.15, 5.81, 5.70, 5.65, 5.33, 5.62, 5.19, 6.13, 7.20, 7.34, 7.95, 7.53, 7.39, 7.59, 7.27 ]

def max_price(a, b):
    result = max(stock_prices[(a - 1) : b])
    return result

def min_price(a, b):
    result = min(stock_prices[(a - 1) : b])
    return result

def price_at(x):
    result = stock_prices[x - 1]
    return result

print(max_price(1, 15))
print(min_price(5, 10))
print(price_at(3))