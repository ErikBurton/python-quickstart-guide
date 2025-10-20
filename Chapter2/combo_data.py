# Daily high and low temps (in Farenheit)
temps = [
    [
        [66, 34],
        [57, 25],
        [49, 45],
        [41, 51],
        [64, 51],
        [67, 57],
        [69, 42]
    ],
    [
        [52, 39],
        [61, 51],
        [64, 51],
        [67, 57],
        [69, 42],
        [32, 14],
        [49, 37]
    ]
]
# Week 1 - Day 1 temps
print(f"Week 1 - Day 1 temps: {temps[0][0]}")

# Week 1 - Day 2 temps
print(f"Week 1 - Day 2 temps: {temps[0][1]}")

# Week 1 - Day 1 high
print(f"Week 1 - Day 1 high: {temps[0][0][1]}")

# Week 1 - Day 2 low
print(f"Week 1 - Day 2 low: {temps[0][1][0]}")

# Week 2 Day 5 high
print(f"Week 2 - Day 5 high: {temps[1][4][0]}")

# Week 2 Day 5 low
print(f"Week 2 - Day 5 low: {temps[1][4][1]}")

# Week 1 temps
print("Week 1 temps:")
for day, (high, low) in enumerate(temps[0], start=1):
    print(f"  Day {day}: High = {high}, Low = {low}")

# Week 2 temps
print("\nWeek 2 temps:")
for day, (high, low) in enumerate(temps[1], start=1):
    print(f"  Day {day}: High = {high}, Low = {low}")
