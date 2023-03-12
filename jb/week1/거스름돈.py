balance = 1260

coins = [500, 100, 50, 10]
answer = 0

for coin in coins :
    answer += balance // coin
    balance %= coin

print(answer)