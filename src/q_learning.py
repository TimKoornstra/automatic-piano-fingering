## Q-Learning is described here

# Imports
import numpy as np
import environment as env
import note_parser

# Code
lowest_note = -8
highest_note = 48
total_range = highest_note - lowest_note

# We want an array that maps each note to another note with q_values for each finger.
# We double the total range so that we can fit the semitones in as well.
# q_values[previous_note, next_note, finger]
q_values = np.zeros((total_range * 2, total_range * 2, total_range * 2, 5))


def train(data):
    global q_values

    # Define training parameters
    epsilon = 0.9  # How often we should take the best action
    discount_factor = 0.9  # The discount factor for future rewards
    learning_rate = 0.1  # How fast our agent learns
    episodes = 1000  # How many episodes we train for

    # Parse the data from a data frame to numerical values
    notes = note_parser.to_numerical(data)
    notes = [int((x - lowest_note) * 2) for x in notes]

    # Train for x amount of episodes
    for _ in range(episodes):
        previous_finger = -1

        # Continue until the end of the sheet
        for i in range(len(notes)):
            # Choose the best finger
            if i == 0:
                action_index = env.get_next_action(
                    None, notes[i], notes[i + 1], epsilon
                )
            elif i == len(notes) - 1:
                action_index = env.get_next_action(
                    notes[i - 1], notes[i], None, epsilon
                )
            else:
                action_index = env.get_next_action(
                    notes[i - 1], notes[i], notes[i + 1], epsilon
                )

            # Calculate reward and temporal difference and transition to next state
            reward = env.calculate_reward(
                notes[i] / 2 + lowest_note, previous_finger, action_index
            )
            previous_finger = action_index

            # If this is not the first note
            if i != 0 and i != len(notes) - 1:
                old_q = q_values[notes[i - 1], notes[i], notes[i + 1], action_index]
                temporal_difference = (
                    reward
                    + discount_factor
                    * np.max(q_values[notes[i - 1], notes[i], notes[i + 1]])
                    - old_q
                )

                # Update the Q-Value
                new_q = old_q + (learning_rate * temporal_difference)
                q_values[notes[i - 1], notes[i], notes[i + 1], action_index] = new_q

    print(f"Done training after {episodes} episodes!")


def find_optimal_fingering(data):
    ret_val = []
    # Parse the data from a data frame to numerical values
    notes = note_parser.to_numerical(data)
    notes = [int((x - lowest_note) * 2) for x in notes]

    for i in range(len(notes)):
        if i == 0:
            action_index = env.get_next_action(None, notes[i], notes[i + 1], 1)
        elif i == len(notes) - 1:
            action_index = env.get_next_action(notes[i - 1], notes[i], None, 1)
        else:
            action_index = env.get_next_action(notes[i - 1], notes[i], notes[i + 1], 1)

        ret_val.append(env.actions[action_index])

    return ret_val
