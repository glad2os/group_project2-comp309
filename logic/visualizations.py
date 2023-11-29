import matplotlib.pyplot as plt
import seaborn as sns
import io


def create_plot(data):
    plt.figure(figsize=(10, 6))
    sns.countplot(x='OCC_YEAR', data=data)
    # Generate the plot
    buf = io.BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)
    return buf
