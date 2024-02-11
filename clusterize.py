import argparse
import pandas as pd
import yaml
import numpy as np
from model import Model

if "__main__" == __name__:
    parser = argparse.ArgumentParser(description="If run wth --all .yaml file must be provided")
    parser.add_argument("--data", type=str, required=True, help="Path to the dataset")
    parser.add_argument("--algo", type=str, required=True, help="The name of the algorithm for clustering")
    parser.add_argument("--config_path", type=str, help="Path to the .yaml file with algo parameters")

    args = parser.parse_args()
    df = pd.read_csv(args.data)
    if args.algo == "all":
        with open('clustering_config.yaml', 'r') as f:
            data = yaml.load(f, Loader=yaml.SafeLoader)
        print(data)
        model = Model()
        results = []
        result_df = pd.DataFrame(columns=['Name', 'Silhouette coefficient'])
        for algorithm, parameters in data.items():
            model = Model(algorithm, parameters)
            picture = model.get_picture()
            silhouette_coef = model.get_silhouette_coef(df)
            results.append((silhouette_coef, picture))
            new_row = {'name': algorithm, 'Silhouette coefficient': silhouette_coef}
            result_df = df.append(new_row, ignore_index=True)

        csv_file_path = 'all_model_results.csv'
        result_df.to_csv(csv_file_path, index=False)

    elif args.config_path is not None:
        with open('clustering_config.yaml', 'r') as f:
            data = yaml.load(f, Loader=yaml.SafeLoader)
            model = Model(data)
            silhouette = model.get_silhouette(df)
            picture = model.get_picture()
            print("Your model silhouette coefficent is", model.get_silhouette_coef)
    else:
        pass
