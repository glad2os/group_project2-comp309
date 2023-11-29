import numpy as np
import pandas as pd


def find_most_repetitive(df_summary):
    most_repetitive_data = {}
    for column in df_summary:
        if df_summary[column].get('unique', 0) > 0:
            most_repetitive_data[column] = {
                'Top': df_summary[column]['top'],
                'Frequency': df_summary[column]['freq']
            }

    return most_repetitive_data


def find_interesting_numerical_data(df_summary):
    interesting_data = {}
    for column in df_summary:
        if pd.notnull(df_summary[column].get('mean')):
            interesting_data[column] = {
                'Mean': df_summary[column]['mean'],
                'Standard Deviation': df_summary[column]['std'],
                'Min': df_summary[column]['min'],
                'Max': df_summary[column]['max']
            }
    return interesting_data


def describe_data(data):
    df = pd.DataFrame(data)
    repetitive_data = {}
    numerical_data = {}

    for column in df:
        if df[column].dtype == 'object':
            top_value = df[column].value_counts().idxmax()
            frequency = df[column].value_counts().max()
            repetitive_data[column] = {
                'Top': top_value,
                'Frequency': int(frequency)
            }
        else:
            numerical_data[column] = {
                'Mean': float(df[column].mean()),
                'Standard Deviation': float(df[column].std()),
                'Min': float(df[column].min()),
                'Max': float(df[column].max())
            }

    findings = {
        'Most Repetitive Data': repetitive_data,
        'Interesting Numerical Data': numerical_data
    }

    return findings


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
