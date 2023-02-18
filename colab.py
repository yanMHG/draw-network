import matplotlib.pyplot as plt


def colab_context(figsize=(20, 10), dpi=100):
    return plt.rc_context({"figure.figsize": figsize, "figure.dpi": dpi})
