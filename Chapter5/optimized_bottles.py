# Define the bottles_song function
# with the start argument defaulting to 99

def bottles_song(start=99):
    # Set the initial number of bottles to the start argument
    bottles = start
    # Loop through until bottles are gone
    while bottles > 0:
        # Display the song
        this_verse = []
        this_verse.append(str(bottles) + " bottles of beer on the wall. ")
        this_verse.append(str(bottles) + " bottles of beer. ")
        this_verse.append("Take on down, pass it around, ")
        # Subtract a bottle
        bottles -= 1
        this_verse.append(str(bottles) + " bottles of beer on the wall. ")
        # Yield to calling function
        yield "".join(this_verse)
        # Pick back up here when we return
    return True


# Loop throuh the generator
for v in bottles_song():
    print(v)
