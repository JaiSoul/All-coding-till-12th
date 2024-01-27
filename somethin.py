gravity = 3
anti_gravity = -3
bally = 300
if bally < 510 and bally > 50:
    while bally <= 50:
        bally += anti_gravity
        print(bally)
if bally < 50:
    while bally >= 510:
        bally += gravity
        print(bally)