import matplotlib.pyplot as plt


class ColabContext:
    def __init__(self, dpi=100):
        self.dpi = dpi

    def __enter__(self):
        self.plt_context = plt.rc_context({"figure.dpi": self.dpi})
        self.plt_context.__enter__()

    def __exit__(self, type, value, traceback):
        pass
