from matplotlib import colors
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.ticker as ticker


def draw(
    ax,
    title,
    name,
    function,
    values,
    x_range,
    y_range,
    colors=tuple(colors.TABLEAU_COLORS),
    cmap=None,
):
    X, Y = np.meshgrid(x_range, y_range)

    ax.set_title(title)

    ax.set_xlabel("x")
    ax.set_ylabel("y")

    ax.grid(color="black", linestyle="-", linewidth=0.5, which="major")
    ax.grid(color="grey", linestyle="--", linewidth=0.25, which="minor")

    ax.xaxis.set_major_locator(ticker.MultipleLocator(base=1))
    ax.yaxis.set_major_locator(ticker.MultipleLocator(base=1))
    ax.minorticks_on()

    CS = ax.contour(X, Y, function(X, Y), values, colors=colors, cmap=cmap)

    def fmt(x):
        s = f"{x:.1f}"
        if s.endswith("0"):
            s = f"{x:.0f}"
        return rf"{name}={s}"

    ax.clabel(CS, inline=True, fontsize=10, fmt=fmt)


def q1b():

    figure, (a1, a2) = plt.subplots(1, 2, figsize=(18, 9))

    x_values = np.arange(-2.5, 2.5, 0.1)
    y_values = np.arange(-2.5, 2.5, 0.1)
    curve_values = np.arange(-5, 6, 0.5)

    draw(
        a1,
        "U curves",
        "u",
        lambda x, y: x * y,
        curve_values,
        x_values,
        y_values,
    )

    draw(
        a2,
        "V curves",
        "v",
        lambda x, y: x**2 - y**2,
        curve_values,
        x_values,
        y_values,
    )

    plt.savefig("./A1/Q1B.png", transparent=True, dpi=100, bbox_inches="tight")


if __name__ == "__main__":
    q1b()
