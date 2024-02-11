import argparse
import pandas as pd
import yaml
import numpy as np
from sklearn.cluster import KMeans
from sklearn.cluster import DBSCAN
from sklearn.cluster import SpectralClustering
from sklearn.mixture import GaussianMixture
from model import Model

def get_alg_name(name):
    algorithms = {"KMeans": KMeans(),
                  "DBSCAN": DBSCAN(),
                  "SpectralClustering": SpectralClustering(),
                  "GaussianMixture": GaussianMixture()}
    return algorithms[name]

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
        results = []
        result_df = pd.DataFrame(columns=['Name', 'Silhouette coefficient'])
        for algorithm, parameters in data.items():
            model = Model(get_alg_name(algorithm), parameters)
            results.append(model.get_results())
            new_row = {'name': algorithm, 'Silhouette coefficient': model.silhouette_coef()}
            result_df = df.append(new_row, ignore_index=True)

        csv_file_path = 'all_model_results.csv'
        result_df.to_csv(csv_file_path, index=False)

    elif args.config_path is not None:
        with open('clustering_config.yaml', 'r') as f:
            parameters = yaml.load(f, Loader=yaml.SafeLoader)
        algorithm = args.algo
        model = Model(get_alg_name(algorithm), parameters)
        results = model.get_results()
        print("Your model silhouette coefficent is", results[0])
    else:
        model = get_alg_name(args.algo)
        params = model.get_params().keys()
        params_as_input = ["--" + value + "\n" for value in params]
        line = "Please insert values for any of these attributes (default values will be used otherwise)"
        show_line = line + "\n" + "".join(params_as_input) + "\n"
        user_input = input(show_line)
        params_list = user_input.split(" ")
        params_dict = {}
        for i in range(0, len(params_list), 2):
            key = params_list[i][2:]
            value = params_list[i+1]
            params_dict[key] = value

