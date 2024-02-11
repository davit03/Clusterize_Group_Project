import yaml

# Data to be written to the YAML file
if "__main__" == __name__:
    data = {
        'KMeans': {
            'n_clusters': 10,
            'init': 'random',
            'max_iter': 40
        },
        'Spectral': {
            'n_clusters': 8,
            'gamma': 1.1,
            'affinity': 'rbf'
        }
    }

    # File path to save the YAML file
    file_path = 'clustering_config.yaml'

    # Writing data to YAML file
    with open(file_path, 'w') as file:
        yaml.dump(data, file)

    print(f"YAML file '{file_path}' has been generated successfully.")