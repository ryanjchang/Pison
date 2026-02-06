import numpy as np
import pandas as pd

class clean_data():
    @staticmethod
    def clean(df, type):
        """
        cleans data by filter by test type,
        removing zeroes based on type,
        removes null values
        removes duplicates
        """
        # remove other test types
        df = clean_data.filter_type(df, type)
        # remove zeros
        if type == "READY" or type == "AGILITY":
            df = clean_data.remove_zeros(df)
        # remove null
        df = df.dropna(subset=['score'])
        # remove duplicates
        df = df.drop_duplicates()

        return df
    @staticmethod
    def filter_type(df, type):
        return df[df['type'] == type]

    @staticmethod
    def remove_zeros(df):
        # convert 0 strings in numerical 0s
        df = df.copy()
        df['score'] = pd.to_numeric(df['score'], errors='coerce')
        return df[df['score'] != 0]