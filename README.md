# Bachelor Thesis Repository
This page contains the code and planning for my (Tim Koornstra) Bachelor Thesis.
## About the code
This code allows the user to input a number of music sheets in the MusicXML file format, which will be trained using the epsilon-greedy Q-Learning algorithm. The output of the program will be a pandas dataframe with each of the notes from the right hand, along with their predicted optimal fingering.
## Installation
`$ pip install pandas`
This should install pandas, as well as numpy. If numpy has node been installed, run:
`$ pip install numpy`
## How to run
Clone the repository. Upload any new xml files to the "data" folder. In main.py follow the example and change to train and test on the desired dataframes.

