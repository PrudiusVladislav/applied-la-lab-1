from matplotlib import pyplot as plt


def plot_object(obj, title=""):
    plt.figure()
    plt.fill(obj[:, 0], obj[:, 1], edgecolor='b', fill=False)
    plt.title(title)
    plt.grid(True)
    plt.show()


def plot_objects(obj1, obj2, main_title, title1="", title2=""):
    plt.figure()

    plt.subplot(1, 2, 1)
    plt.fill(obj1[:, 0], obj1[:, 1], edgecolor='b', fill=False)
    plt.title(title1)
    plt.grid(True)

    plt.subplot(1, 2, 2)
    plt.fill(obj2[:, 0], obj2[:, 1], edgecolor='b', fill=False)
    plt.title(title2)
    plt.grid(True)

    plt.suptitle(main_title)
    plt.show()
