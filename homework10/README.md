# Homework 10 - MLOps with a Linear Classifier

This project builds on Homework 09 by taking the breast cancer linear classifier and putting it into production. It fits two models, saves them to disk, and provides a script to make predictions on new sample data.

## Data Preparation and Model Performance

### Model 1: Plain Linear Classifier
The breast cancer dataset was loaded from sklearn, split into 70% training and 30% test data, and fit using a linear classifier with the Perceptron algorithm. No preprocessing was applied to the data.

- Test accuracy: 0.9181
- Train accuracy: 0.8894

### Model 2: Normalized Pipeline
The same data split was used, but this time the data was normalized using a StandardScaler before being passed to the classifier. This puts all features on the same scale before classification.

- Test accuracy: 0.9649
- Train accuracy: 0.9899

The pipeline performed better on both training and test data, suggesting that normalizing the data helps the classifier.

## Usage

First, run the training script to fit the models and save them to disk:

```bash
python3 training.py
```

Then, run the inference script with a sample data CSV file:

```bash
python3 inference.py --sample_data sample_data.csv
```

The sample data CSV should contain one or more rows of the 30 breast cancer features with a header row. A sample file is provided in this directory.

Example output:
Your sample data contains 1 entry:
non-normalized model predicts: [0]
normalized model in pipeline predicts: [0]

Where 0 = malignant and 1 = benign.
