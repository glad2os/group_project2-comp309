import matplotlib
import matplotlib.pyplot as plt
import seaborn as sns
import io

matplotlib.use('Agg')


def create_plot(data):
    year_counts = data['OCC_YEAR'].value_counts().reset_index()
    year_counts.columns = ['OCC_YEAR', 'count']
    threshold = 10
    filtered_year_counts = year_counts[year_counts['count'] >= threshold]
    plt.figure(figsize=(10, 6))
    sns.barplot(x='OCC_YEAR', y='count', data=filtered_year_counts)
    buf = io.BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)
    return buf
