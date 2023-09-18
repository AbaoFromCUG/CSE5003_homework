import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch
from mpl_toolkits.mplot3d.proj3d import proj_transform
from mpl_toolkits.mplot3d.axes3d import Axes3D


#---------------------begin----------------------
# copy from https://gist.github.com/WetHat/1d6cd0f7309535311a539b42cccca89c
# for 3d arrow draw
# @Abao Zhang

class Arrow3D(FancyArrowPatch):

    def __init__(self, x, y, z, dx, dy, dz, *args, **kwargs):
        super().__init__((0, 0), (0, 0), *args, **kwargs)
        self._xyz = (x, y, z)
        self._dxdydz = (dx, dy, dz)

    def draw(self, renderer):
        x1, y1, z1 = self._xyz
        dx, dy, dz = self._dxdydz
        x2, y2, z2 = (x1 + dx, y1 + dy, z1 + dz)

        xs, ys, zs = proj_transform((x1, x2), (y1, y2), (z1, z2), self.axes.M)
        self.set_positions((xs[0], ys[0]), (xs[1], ys[1]))
        super().draw(renderer)
        
    def do_3d_projection(self, renderer=None):
        x1, y1, z1 = self._xyz
        dx, dy, dz = self._dxdydz
        x2, y2, z2 = (x1 + dx, y1 + dy, z1 + dz)

        xs, ys, zs = proj_transform((x1, x2), (y1, y2), (z1, z2), self.axes.M)
        self.set_positions((xs[0], ys[0]), (xs[1], ys[1]))

        return np.min(zs) 



def _arrow3D(ax, x, y, z, dx, dy, dz, *args, **kwargs):
    '''Add an 3d arrow to an `Axes3D` instance.'''

    arrow = Arrow3D(x, y, z, dx, dy, dz, *args, **kwargs)
    ax.add_artist(arrow)


setattr(Axes3D, 'arrow3D', _arrow3D)

#---------------------end----------------------


def draw_samples(samples):
    """
        Draw points in picture
            samples must be np.array with shape (n, 2)
    """
    
    ax = plt.figure().add_subplot(projection='3d')
    ax.scatter(samples[:, 0], samples[:, 1], samples[:, 2], s=100)
    plt.show()
    
def draw_path(points):
    """
        Draw path with arrow, and annotate the start city
    """
    ax = plt.figure().add_subplot(projection='3d')
    ax.set_box_aspect((np.ptp(points[:, 0]), np.ptp(points[:, 1]), np.ptp(points[:, 2])))
    ax.scatter(points[:, 0], points[:, 1], points[:, 2], c= "green", s=50)
    for i in range(len(points) - 1):
        p1, p2 = points[i], points[i + 1]
        ax.arrow3D(*p1, *(p2-p1), mutation_scale=20, fc='black')
        
    # start point
    ax.scatter(*points[0], c = "red", s=120)
    plt.show()
