# Define the bottles_song function
# with the start argument defaulting to 99

def bottles_song(start=99):
    # Set the initial number of bottles to the start argument
    bottles = start
    # Loop through until bottles are gone
    while bottles > 0:
        # Display the song
        verse = str(bottles) + " bottles of beer on the wall. "
        verse += str(bottles) + " bottles of beer. "
        verse += "Take on down, pass it around, "
        # Subtract a bottle
        bottles -= 1
        verse += str(bottles) + " bottles of beer on the wall. "
        # Yield to calling function
        yield verse
        # Pick back up here when we return
    return True


# Loop throuh the generator
for v in bottles_song():
    print(v)
