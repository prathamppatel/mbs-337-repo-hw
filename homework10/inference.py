#!/usr/bin/env python3

import argparse
import logging
import pickle
import socket
import pandas as pd

format_str = (
    f'[%(asctime)s {socket.gethostname()}] '
    '%(filename)s:%(funcName)s:%(lineno)s - %(levelname)s: %(message)s'
)

parser = argparse.ArgumentParser()
parser.add_argument('--sample_data', type=str, required=True,
                    help='path to sample data csv file')
parser.add_argument('-l', '--loglevel',
                    type=str,
                    required=False,
                    default='WARNING',
                    help='set log level to DEBUG, INFO, WARNING, ERROR, or CRITICAL')
args = parser.parse_args()

logging.basicConfig(level=args.loglevel, format=format_str)

try:
    logging.info('Loading classifier model')
    with open('classifier.pkl', 'rb') as f:
        clf = pickle.load(f)

    logging.info('Loading pipeline model')
    with open('normalizer_and_data_classifier_pipeline.pkl', 'rb') as f:
        pipeline = pickle.load(f)

    logging.info(f'Loading sample data from {args.sample_data}')
    data = pd.read_csv(args.sample_data)

    logging.info('Making predictions')
    pred_clf = clf.predict(data.values)
    pred_pipeline = pipeline.predict(data.values)

    print(f'Your sample data contains {len(data)} entry:')
    print(f'non-normalized model predicts: {pred_clf}')
    print(f'normalized model in pipeline predicts: {pred_pipeline}')

except FileNotFoundError as e:
    logging.error(f'File not found: {e}')