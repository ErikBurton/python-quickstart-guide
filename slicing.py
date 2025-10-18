greeting = "Well, hello there!"
hello = greeting[6:11]  # Index starts at 0, so W=0, e=1 and so on....h=6
print(hello)

greeting = "Well, hello there!"
hello = greeting[6:]
# Omiting the 2nd number after the :, it will finish the rest of the string.
# hello there!
print(hello)

greeting = "Well, hello there!"
hello = greeting[:4]
# Omiting the 1st number before the :, we will see the begining of the string.
# Well
print(hello)
