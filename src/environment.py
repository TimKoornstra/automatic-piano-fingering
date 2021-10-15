### Environment for the RL is described here

## Imports
import pandas as pd
import numpy as np
import q_learning as q
from xml.dom import minidom

## States
def create_dataframe(file):
    """
        This function reads an MusicXML file and processes it into a pandas data frame.
        Works for music in all keys.
    """
    
    df = pd.DataFrame(columns=["step","alter","octave"])
    mysheet = minidom.parse(file)
    notes = mysheet.getElementsByTagName("note")
    index = 0

    for i in range(len(notes)):
        pitchNode = notes[i].getElementsByTagName("pitch")
        voiceNode = notes[i].getElementsByTagName("voice")[0].childNodes[0].nodeValue
        tieNode = notes[i].getElementsByTagName("tie")

        # If it is not a rest or on the right hand
        if (len(pitchNode) > 0 and pitchNode[0].nodeName == "pitch" and voiceNode == "1"):
            if ((len(tieNode) > 0 and tieNode[0].getAttributeNode("type").nodeValue == "start") or len(tieNode) == 0):
                step = pitchNode[0].getElementsByTagName("step")[0].childNodes[0].nodeValue
                octave = pitchNode[0].getElementsByTagName("octave")[0].childNodes[0].nodeValue
                alter = pitchNode[0].getElementsByTagName("alter")

                if (len(alter) > 0):
                    if (alter[0].childNodes[0].nodeValue == "1"):
                        alter = "#"
                    else:
                        alter = "b"
                else:
                    alter = ""

                df.loc[index] = [step] + [alter] + [octave]
                index += 1

    # End the data frame
    df.loc[len(df)] = ["fin"] + ["fin"] + ["fin"]

    return df

# Create the hand that we are going to use. All data is initialized to "None", since the initial
# location of the hand should be determined by the first note that is played.
hand = [None, None, None, None, None]

## Actions
# The agent has the option of choosing one of five fingers on the right hand.
# i.e. actions[0] is the thumb, actions[1] is the index finger, etc.
actions = ["1", "2", "3", "4", "5"]

def get_next_action(previous_note, current_note, next_note, epsilon):
    if np.random.random() < epsilon and previous_note != None and next_note != None:          # Take the best finger
        return np.argmax(q.q_values[previous_note, current_note, next_note])
    elif np.random.random() < epsilon and previous_note == None:
        return np.argmax(q.q_values[0, current_note, next_note])
    elif np.random.random() < epsilon and next_note == None:
        return np.argmax(q.q_values[previous_note, current_note, len(q.q_values) - 1])
    else:                                                                                     # Take a random finger
        return np.random.randint(5)

## Rewards
def calculate_reward(note_played, previous_finger, finger):
    """
        Calculate the reward/penalty for playing a note with a finger.

        The "note_played" argument is a floating point value. The "finger" input is the finger number.
    """
    # General idea:
    # Look up the location of the used finger and determine the distance from that location to the new location.
    # The score will be the distance from the finger location to the new note.
    # When we have calculated the reward/penalty, we reposition the hand and return the reward/penalty.

    # If this is the initial note, we want to return 0 (no cost for the first placement) but also reposition the hand.
    if (hand[0] == None):
        reposition_hand(note_played, finger)
        return 0
    else:
        distance = abs(note_played - hand[finger])
        reward = -distance

        reposition_hand(note_played, finger)
        return reward


def reposition_hand(note_played, finger):
    """
        Reposition the hand to a new position. The new location is determined by the played note and the finger used.

        The "note_played" argument is a floating point value. The "finger" input is the finger number.
    """

    global hand
    natural_note = int(note_played)
    hand = [n - finger + natural_note for n in range(5)]
    hand[finger] = note_played

    return hand
