from sklearn.model_selection import train_test_split

def split_data(data, labels, test_size=0.2, random_state=42):
    """
    Splits the data into training and testing sets.

    Args:
        data (list): The data to be split.
        labels (list): The corresponding labels for the data.
        test_size (float, optional): The proportion of the dataset to include in the test split. Defaults to 0.2.
        random_state (int, optional): The seed used by the random number generator. Defaults to 42.

    Returns:
        tuple: The training data, testing data, training labels, and testing labels.
    """
    X_train, X_test, y_train, y_test = train_test_split(data, labels, test_size=test_size, random_state=random_state)
    return X_train, X_test, y_train, y_test