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

# Cluster_2
cluster_2 = ['100BNP', '100BRP', '100BLP', '101BNP', '101BRP', '103BNP', '103BRP', '106BNP', '106BRP',
                 '111BNP', '111BRP', '115BNP', '115BRP', '108BNP', '108BRP', '108BLP', '113BNP', '113BRP', '113BLP',
                 '110BNP', '110BRP']
df = draw_and_remove_elements(cluster_2, seed=41)
print(df)

# Cluster_3
cluster_3 = ['112BNP', '112BRP', '112BLP', '112BLPRP', '119BNP', '119BRP', '119BLP', '114BNP', '114BRP', '114BLP', '114BLPRP', '114BLP2xRP', '121BNP', '121BRP', '123BNP', '123BRP']
df = draw_and_remove_elements(cluster_3, seed=40)
print(df)

# Cluster_4
cluster_4 = ['116BNP', '116BRP', '116BLP', '116BLPRP', '125BNP', '125BRP', '125BLP', '127BNP', '127BRP']
df = draw_and_remove_elements(cluster_4, seed=39)
print(df)

# Cluster_5
cluster_5 = ['128BNP', '128BRP', '128BLP']
df = draw_and_remove_elements(cluster_5, seed=38)
print(df)
