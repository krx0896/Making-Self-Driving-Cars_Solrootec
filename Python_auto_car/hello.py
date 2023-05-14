n = 800
count = 0
coin_types = [500, 500, 300]
for coin in coin_types:
    count += n // coin
    n %= coin

    print(count)
