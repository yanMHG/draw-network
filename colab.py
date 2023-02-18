import matplotlib.pyplot as plt


def colab_context(figsize=(20, 10), dpi=100, fontsize=6):
    return plt.rc_context(
        {"figure.figsize": figsize, "figure.dpi": dpi, "font.size": fontsize}
    )
