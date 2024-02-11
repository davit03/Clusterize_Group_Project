import argparse

if "__main__" == __name__:
    parser = argparse.ArgumentParser(description="If run wth --all .yaml file must be provided")
    parser.add_argument("--data", type=str, required=True, help="Path to the dataset")
    parser.add_argument("--algo", type=str, required=True, help="The name of the algorithm for clustering")
    parser.add_argument("--config_path", type=str, help="Path to the .yaml file with algo parameters")

