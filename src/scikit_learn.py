from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.preprocessing import OneHotEncoder
import pandas as pd


def convert_to_encoded(data):
    one_hot_encoder = OneHotEncoder()
    x = one_hot_encoder.fit_transform(data['adjClose'].values.reshape(-1, 1)).toarray()
    df_one_hot = pd.DataFrame(x)
    df = pd.concat([data, df_one_hot], axis=1)
    df = df.drop(['adjClose'], axis=1)
    print(df)


def generate_test_train_split(x, y):
    return train_test_split(x, y, random_state=1)


def classify_data(x_train, x_test, y_train, y_test):
    tree = DecisionTreeClassifier(max_depth=7, random_state=0)
    tree.fit(x_train, y_train)
    tree.score(x_test, y_test)
