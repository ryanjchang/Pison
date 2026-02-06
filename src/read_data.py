class read_data():
    @staticmethod
    def get_file():
        """
        Example: data/all_data.csv
        """
        return input("Please enter file path:\n")

    @staticmethod
    def get_type():
        type = input("Please select test type (readiness, agility, focus):\n")
        if type.lower() in ("r", "ready", "readiness"):
            return "READY"
        elif type.lower() in ("a", "agility"):
            return "AGILITY"
        elif type.lower() in ("f", "focus"):
            return "FOCUS"
        raise ValueError("Invalid test type")