#!/usr/bin/env python3

import logging
import pickle
import argparse
import socket

from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import SGDClassifier
from sklearn.metrics import accuracy_score
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler

format_str = (
    f'[%(asctime)s {socket.gethostname()}] '
    '%(filename)s:%(funcName)s:%(lineno)s - %(levelname)s: %(message)s'
)

parser = argparse.ArgumentParser()
parser.add_argument('-l', '--loglevel',
                    type=str,
                    required=False,
                    default='WARNING',
                    help='set log level to DEBUG, INFO, WARNING, ERROR, or CRITICAL')
args = parser.parse_args()

logging.basicConfig(level=args.loglevel, format=format_str)


def load_data() -> tuple:
    """
    Load the breast cancer dataset from sklearn.

    Returns:
        X: Independent variables as a numpy array.
        y: Dependent variables as a numpy array.
    """
    logging.info('Loading breast cancer dataset')
    data = load_breast_cancer()
    X = data.data
    y = data.target
    return X, y


def split_data(X, y) -> tuple:
    """
    Split the data into training and test datasets.

    Args:
        X: Independent variables as a numpy array.
        y: Dependent variables as a numpy array.

    Returns:
        X_train, X_test, y_train, y_test: Split datasets.
    """
    logging.info('Splitting data into training and test sets')
    return train_test_split(X, y, test_size=0.3, stratify=y, random_state=1)


def fit_classifier(X_train, y_train):
    """
    Fit a linear classifier using the Perceptron algorithm.

    Args:
        X_train: Training independent variables.
        y_train: Training dependent variables.

    Returns:
        clf: Trained linear classifier.
    """
    logging.info('Fitting linear classifier')
    clf = SGDClassifier(loss="perceptron", alpha=0.01)
    clf.fit(X_train, y_train)
    return clf


def fit_pipeline(X_train, y_train):
    """
    Fit a pipeline that normalizes data then applies a linear classifier.

    Args:
        X_train: Training independent variables.
        y_train: Training dependent variables.

    Returns:
        pipeline: Trained pipeline.
    """
    logging.info('Fitting pipeline with StandardScaler and SGDClassifier')
    pipeline = Pipeline([
        ('scaler', StandardScaler()),
        ('classifier', SGDClassifier())
    ])
    pipeline.fit(X_train, y_train)
    return pipeline


def save_model(model, filename: str) -> None:
    """
    Save a model to a file using pickle.

    Args:
        model: Trained model or pipeline to save.
        filename: Name of the file to save the model to.

    Returns:
        None
    """
    logging.info(f'Saving model to {filename}')
    with open(filename, 'wb') as f:
        pickle.dump(model, f)


def main():
    try:
        X, y = load_data()
        X_train, X_test, y_train, y_test = split_data(X, y)

        clf = fit_classifier(X_train, y_train)
        accuracy_test = accuracy_score(y_test, clf.predict(X_test))
        accuracy_train = accuracy_score(y_train, clf.predict(X_train))
        logging.info(f'classifier test accuracy = {accuracy_test}')
        logging.info(f'classifier train accuracy = {accuracy_train}')
        print(f'classifier test accuracy = {accuracy_test}')
        print(f'classifier train accuracy = {accuracy_train}')
        save_model(clf, 'classifier.pkl')

        pipeline = fit_pipeline(X_train, y_train)
        pipeline_accuracy_test = accuracy_score(y_test, pipeline.predict(X_test))
        pipeline_accuracy_train = accuracy_score(y_train, pipeline.predict(X_train))
        logging.info(f'pipeline test accuracy = {pipeline_accuracy_test}')
        logging.info(f'pipeline train accuracy = {pipeline_accuracy_train}')
        print(f'pipeline test accuracy = {pipeline_accuracy_test}')
        print(f'pipeline train accuracy = {pipeline_accuracy_train}')
        save_model(pipeline, 'normalizer_and_data_classifier_pipeline.pkl')

    except Exception as e:
        logging.error(f'Error: {e}')

if __name__ == '__main__':
    main()