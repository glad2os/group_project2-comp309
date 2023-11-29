import numpy as np


def describe_data(data):
    return data.describe(include='all')


def statistical_assessments(data):
    numeric_data = data.select_dtypes(include=[np.number])
    means = numeric_data.mean()
    correlations = numeric_data.corr()
    return {
        "means": means.to_dict(),
        "correlations": correlations.to_dict()
    }


def missing_data_evaluation(data):
    return data.isnull().sum()
