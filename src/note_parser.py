# Translating notes to data we can use happens here

## Code
def to_numerical(input):
    """
        This function takes musical notes as input and converts it to a floating point value list.

        The notes are translated by taking the distance to middle key C4. E.g. C4 will result in 0, B3 will result in -1, and C#4 will result in 0.5.
    """
    full_notes = ["C", "D", "E", "F", "G", "A", "B"]
    distances = []

    for _, note in input.iterrows():
        if (note["step"] != "fin"):
            distance = full_notes.index(note["step"])
            distance = distance + (int(note["octave"]) - 4) * 8
            if (note["alter"] == "#"):
                if (note["step"] == "E" or note["step"] == "B"):
                    distance = distance + 1
                else:
                    distance = distance + 0.5
            elif (note["alter"] == "b"):
                if (note["step"] == "C" or note["step"] == "F"):
                    distance = distance - 1
                else:
                    distance = distance - 0.5

            distances.append(distance)

    return distances
