import random
import pandas as pd

def draw_and_remove_elements(array, seed=None):
    if seed is not None:
        random.seed(seed)

    # List to store the removed elements as rows
    removed_elements_list = []

    while array:
        removed_elements = {'A': None, 'B': None, 'D': None, 'E': None}
        columns = ['A', 'B', 'D', 'E']

        for i, column in enumerate(columns):
            if array:
                index = random.randint(0, len(array) - 1)
                element = array.pop(index)
                removed_elements[column] = element
                print(f"Drawn element for column {column}: {element}")

        removed_elements_list.append(removed_elements)

    # Creating a DataFrame to display the result
    df = pd.DataFrame(removed_elements_list)
    return df


# Cluster_1
cluster_1 = ['104BNP', '104BRP', '104BLP', '109BNP', '109BRP', '102BNP', '102BRP', '105BNP', '105BRP', '107BNP',
                 '107BRP']
df = draw_and_remove_elements(cluster_1, seed=42)
print(df)
