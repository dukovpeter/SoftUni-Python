change = float(input())
change_stotinki = round(change * 100)

coins = [200, 100, 50, 20, 10, 5, 2, 1]

coins_count = 0

for coin in coins:
    while change_stotinki >= coin:
        change_stotinki -= coin
        coins_count += 1

print(coins_count)