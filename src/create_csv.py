class create_csv:
    @staticmethod
    def create_csv(df, file_path):
        if not file_path.endswith(".csv"):
            file_path += ".csv"
        df.to_csv(file_path, index=False)
        print("file created at ", file_path)