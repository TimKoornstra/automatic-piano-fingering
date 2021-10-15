#!/usr/bin/env python3

## Imports
import os
import environment as env
import q_learning as q

## Main code
if __name__ == "__main__":
    # Create the dataframes here
    print("Creating dataframes...")
    train = [
        env.create_dataframe(f"./data/train/{file}")
        for file in os.listdir("./data/train")
        if file.endswith(".xml")
    ]
    test = [
        env.create_dataframe(f"./data/test/{file}")
        for file in os.listdir("./data/test")
        if file.endswith(".xml")
    ]
    print("Done!")

    # Train on the dataframes here
    print("Training Agent...")
    for sheet in train:
        q.train(sheet)

    # Find the optimal fingerings and output them
    for sheet in test:
        output = q.find_optimal_fingering(sheet)
        output.append(None)
        sheet["finger"] = output
        print(f"Found optimal fingering for {sheet.name}:")
        print(sheet[:31])
