# Automatically Generated Piano Fingering using Q-Learning
This repository contains the code for automatically generating piano fingerings using a reinforcement learning agent that uses Q-Learning.
## About the code
This code allows the user to input a number of music sheets in the MusicXML file format, which will be trained using the epsilon-greedy Q-Learning algorithm. The output of the program will be a pandas dataframe with each of the notes from the right hand, along with their predicted optimal fingering. A few MusicXML sheets have been provided and are stored in the `data/train` folder. To test the program, simply follow the "How to run" subsection of this README.
Q-Learning is not good foor generalization and this algorithm works best when the sheets in the test set are part of the training set. This ensures that the reinforcement learning agent has already seen the note combinations and the Q-Values are not empty (which results in standard finger 1).
## Dependencies
The required packages to run this code can be found in the `requirements.txt` file. To run this file, execute the following code block:
```
$ pip install -r requirements.txt 
```
Alternatively, you can install the required packages manually like this:
```
$ pip install <package>
```
## How to run
- Clone the repository
- Place all MusicXML `.xml` files that you want the reinforcement learning agent to train on in the `data/train` folder. Place all the MusicXML `.xml` files that you want the reinforcement learning agent to label in the `data/test` folder.
- Run `$ python src/main.py`
- See result
