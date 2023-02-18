import matplotlib.pyplot as plt


class ColabContext:
    def __init__(self, figsize=(20, 10), dpi=100):
        self.dpi = dpi
        self.figsize = figsize

    def __enter__(self):
        self.plt_context = plt.rc_context(
            {"figure.figsize": self.figsize, "figure.dpi": self.dpi}
        )
        self.plt_context.__enter__()

    def __exit__(self, type, value, traceback):
        return
