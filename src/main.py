#!/usr/bin/env python3

## Imports
import environment as env
import q_learning as q

## Main code
if __name__ == "__main__":
    # Create the dataframes here
    print("Creating dataframes...")
    df1 = env.create_dataframe("../data/the_entertainer.xml")
    print("Done!")

    # Train on the dataframes here
    print("Training...")
    q.train(df1)

    # Find the optimal fingering and output it
    output = q.find_optimal_fingering(df1)
    output.append(None)
    df1["finger"] = output
    print(df1[:31])
