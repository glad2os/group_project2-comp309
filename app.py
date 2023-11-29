from flask import Flask, jsonify
from flask import send_file

from logic.data_loader import load_data
from logic.statistics import statistical_assessments, describe_data, missing_data_evaluation
from logic.visualizations import create_plot

app = Flask(__name__)


# a. Data Description Endpoint
@app.route('/data/description', methods=['GET'])
def data_description():
    data = load_data()
    description = describe_data(data)
    return jsonify(description)


# b. Statistical Assessments Endpoint
@app.route('/data/statistics', methods=['GET'])
def data_statistics():
    data = load_data()
    stats = statistical_assessments(data)
    return jsonify(stats)


# c. Missing Data Evaluation Endpoint
@app.route('/data/missing', methods=['GET'])
def data_missing():
    data = load_data()
    missing_data = missing_data_evaluation(data)
    return missing_data.to_json()


# 4. Visualization Endpoints
@app.route('/data/visualization', methods=['GET'])
def data_visualization():
    data = load_data()
    plot = create_plot(data)
    return send_file(plot, mimetype='image/png')


if __name__ == '__main__':
    app.run()
