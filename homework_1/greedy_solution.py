import numpy as np


def distance(p1, p2):
    return np.linalg.norm(p1-p2)

def cost(path):
    dists = np.linalg.norm(path[:-1]-path[1:], axis=1)
    return np.sum(dists)



def greedy(points, start_index):
    """
        Greedy alglorithms of TSP
            points must be np.array with shape (n, 2)
            start_index must be int in range of [0, n-1]
        return visit path, include back to start city
    """
    visit_sequence = [start_index]
    start_point = points[start_index]
    need_visit = set(range(len(points)))
    need_visit.remove(start_index)
    last_visit = start_index
    while len(need_visit) > 0:
        indexs = list(need_visit)
        need_visit_points = points[indexs]
        dists = np.apply_along_axis(lambda p: distance(
            p, points[last_visit]),  1, need_visit_points)
        next_index = indexs[np.argmin(dists)]
        need_visit.remove(next_index)
        visit_sequence.append(next_index)
        last_visit = next_index

    visit_sequence.append(start_index)
    return points[visit_sequence]


class GreedySolution(object):
    def __init__(self, name = None):
        self.name = name

    def fit(self, points, start_index):
        self.points = points
        visit_sequence = [start_index]
        start_point = points[start_index]
        need_visit = set(range(len(points)))
        need_visit.remove(start_index)
        last_visit = start_index

        while len(need_visit) > 0:
            indexs = list(need_visit)
            need_visit_points = points[indexs]
            dists = np.apply_along_axis(lambda p: np.linalg.norm(
                p - points[last_visit]),  1, need_visit_points)
            next_index = indexs[np.argmin(dists)]
            need_visit.remove(next_index)
            visit_sequence.append(next_index)
            last_visit = next_index
        visit_sequence.append(start_index)
        self.visit_idxs = np.array(visit_sequence)
        self.visit_path = points[visit_sequence]
        # sum all point pairs distance
        # path_dists = np.linalg.norm(
        #     self.visit_path[:-1]-self.visit_path[1:], axis=1)
        self.cost = cost(self.visit_path)


if __name__ == "__main__":
    demo = np.array([
        [0, 0],
        [0, 1],
        [1, 1],
    ])

    print(greedy(demo, 0))
    print(greedy(demo, 1))

    solution = GreedySolution()
    solution.fit(demo, 0)
    assert (solution.cost == (2+np.sqrt(2)))
    print(solution.visit_path)
    print(solution.visit_idxs)
