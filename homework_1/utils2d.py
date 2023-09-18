import matplotlib.pyplot as plt
import numpy as np
from greedy_solution import GreedySolution

from bokeh.models import Arrow,  OpenHead, TeeHead, Label
from bokeh.plotting import figure, show
from bokeh.layouts import layout


def shrink_space(p1, p2, space=0.1):
    d = p2-p1
    nd = d / np.linalg.norm(d)
    return p1+nd*space, p2-nd*space
    pass


def draw_samples(samples):
    """
        Draw points in picture
            samples must be np.array with shape (n, 2)
    """
    fig, ax = plt.subplots(figsize=(4, 4))
    ax.set_xlim([np.min(samples[:, 0])-2, np.max(samples[:, 0])+2])
    ax.set_ylim([np.min(samples[:, 1])-2, np.max(samples[:, 1])+2])
    # start point
    # ax.scatter(samples[0, 0], samples[0, 1], c = "green")
    ax.scatter(samples[:, 0], samples[:, 1])

    # ax.plot(samples[:, 0], samples[:, 1])
    plt.show()


def draw_path(points, *nargs, **kargs):
    """
        Draw path with arrow, and annotate the start city
    """
    p = figure(match_aspect=True, *nargs, **kargs)

    p.circle(*points[0], radius=0.1, color="#4dc99e")
    for i in range(len(points)-1):
        p.add_layout(
            Label(x=points[i, 0], y=points[i, 1], text=str(i), text_align="center"))
    # others city
    p.circle(points[1:-1, 0], points[1:-1, 1], radius=0.1)

    oh = OpenHead(line_color="#ebc8ce", line_width=5)
    nh = TeeHead(line_color="#ebc8ce", line_width=5)
    for i in range(len(points) - 1):
        start, end = shrink_space(points[i], points[i+1])
        p.add_layout(Arrow(end=oh, start=nh, line_color="#ebc8ce", line_width=4, line_join="dd",
                     x_start=start[0], y_start=start[1], x_end=end[0], y_end=end[1]))
    return p


def draw_solution(solution: GreedySolution):
    points = solution.points
    p = figure(match_aspect=True,
               title=f"{solution.name}, Cost={solution.cost}")
    visit_path = solution.visit_path
    # start city
    p.circle(*visit_path[0], radius=0.1, color="#4dc99e")
    for i in range(len(visit_path[:-1])):
        p.add_layout(
            Label(x=visit_path[i, 0], y=visit_path[i, 1], text=str(i), text_align="center"))
    # others city
    p.circle(visit_path[1:-1, 0], visit_path[1:-1, 1], radius=0.1)

    oh = OpenHead(line_color="#ebc8ce", line_width=5)
    nh = TeeHead(line_color="#ebc8ce", line_width=5)
    for i in range(len(solution.visit_path) - 1):
        start, end = shrink_space(
            solution.visit_path[i], solution.visit_path[i+1])
        p.add_layout(Arrow(end=oh, start=nh, line_color="#ebc8ce", line_width=4, line_join="dd",
                     x_start=start[0], y_start=start[1], x_end=end[0], y_end=end[1]))
    return p
