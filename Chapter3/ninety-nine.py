# bottles = 99
# while bottles > 0:
#     print(str(bottles) + " bottles of beer on the wall.")
#     print(str(bottles) + " bottles of beer.")
#     bottles -= 1
#     print("Take one down, pass it around.")
#     print(str(bottles) + " bottles of beer on the wall.")


for bottles in range(99, 0, -1):
    print(f"{bottles} bottles of beer on the wall.")
    print(f"{bottles} bottles of beer.")
    print("Take on down, pass it around")
    next_bottles = bottles - 1
    if next_bottles > 0:
        print(f"{next_bottles} bottle{'s' if next_bottles > 1 else ''} of beer on the wall.\n")
    else:
        print("No more bottles of beer on the wall!")
