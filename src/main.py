import sys
import numpy as np
import pandas as pd
sys.path.append(".")
from src.clean_data import clean_data
from src.read_data import read_data
from src.create_csv import create_csv

def main():
    # example usage: data/all_data_new_small.csv
    file_name = read_data.get_file()
    test_type = read_data.get_type()

    # read csv
    df = pd.read_csv(file_name)
    # clean data
    df = clean_data.clean(df, test_type)
    # create new csv
    new_file = input("Create new file?\n")

    if new_file.lower() in ("yes, y"):
        file_path = input("File name:\n")
        create_csv.create_csv(df, file_path)

if __name__ == "__main__":
    main()