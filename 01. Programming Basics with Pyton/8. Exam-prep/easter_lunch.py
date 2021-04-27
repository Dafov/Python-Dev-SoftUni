easter_bread = int(input())
eggs = int(input())
cookies = int(input())

easter_bread_price = 3.20
eggs_price = 4.35
cookies_price = 5.40
eggs_paint_price = 0.15
eggs_count = 12

easter_bread_total = 0
eggs_total = 0
cookies_total = 0
eggs_paint_total = 0

for i in range(1, easter_bread + 1):
    easter_bread_total = easter_bread * easter_bread_price
    break

for i in range(1, eggs + 1):
    eggs_total = eggs * eggs_price
    eggs_paint_total = eggs * eggs_count * eggs_paint_price
    break

for i in range(1, cookies + 1):
    cookies_total = cookies * cookies_price
    break

total = easter_bread_total + eggs_total + cookies_total + eggs_paint_total

print(f"{total:.2f}")