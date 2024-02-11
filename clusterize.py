import argparse
import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
from sklearn.cluster import DBSCAN
from sklearn.cluster import SpectralClustering
from sklearn.decomposition import PCA
from sklearn.manifold import TSNE
from sklearn.manifold import MDS

if "__main__" == __name__:
    parser = argparse.ArgumentParser(description="If run wth --all .yaml file must be provided")
    parser.add_argument("--data", type=str, required=True, help="Path to the dataset")
    parser.add_argument("--algo", type=str, required=True, help="The name of the algorithm for clustering")
    parser.add_argument("--config_path", type=str, help="Path to the .yaml file with algo parameters")

    args = parser.parse_args()
    # df = pd.read_csv(args.data)
    if args.algo == "all":
        pass
    elif args.config_path is not None:
        pass
    else:
        # kmeans = KMeans()
        # params = kmeans.get_params(args)
        algorithms = {"KMeans" : KMeans(),
                      "DBSCAN" : DBSCAN(),
                      "SpectralClustering" : SpectralClustering(),
                      "PCA" : PCA(),
                      "MDS" : MDS(),
                      "TSNE" : TSNE()}
        model = algorithms[args.algo]
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
        print(params_dict)