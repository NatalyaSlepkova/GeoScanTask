from itertools import repeat
import sys
from visualization import MyWidget
from PyQt5 import QtWidgets


class SegmentTree:
    def __init__(self, n, array):
        self.vertex_count = 4 * n
        self.array = array
        self.vertexs = [(0, 0)] * self.vertex_count

    def build(self, v, tl, tr):
        if tl == tr:
            self.vertexs[v] = (self.array[tl], tl)
            return
        tm = (tl + tr) // 2
        build(v * 2, tl, tm)
        build(v * 2 + 1, tm + 1, tr)
        if self.vertexs[v * 2][0] > self.vertexs[v * 2 + 1][0]:
            
        self.vertexs[v] = (max(self.vertexs[v * 2], self.vertexs[v * 2 + 1])

    def get_max(self, v, tl, tr, l, r):
        if l > r:
            return 0
        if tl == tr:
            return self.vertexs[v]
        tm = (tl + tr) // 2
        max_l = self.get_max(v * 2, tl, tm, l, min(tm, r))
        max_r = self.get_max(v * 2 + 1, tm + 1, tr, max(l, tm + 1), r)
        return max(max_l, max_r)


def search_water_line(l, r, h_tower):

def count_water(h_tower):
    n = len(h_tower)
    tree = SegmentTree(n, h_tower)
    tree.build(1, 0, n - 1)
    pos_zeros = []
    for i, h in enumerate(h_tower):
        if h == 0:
            pos_zeros.append(i)


    ans1 = h_tower[0]
    l = 0
    h_water_line = [ans1]
    for i in range(1, len(h_tower)):
        if h_tower[i] >= ans1 or i == len(h_tower) - 1 or h_tower[i] == 0:
            ans2 = h_tower[i]
            h_water_line.extend(repeat(min(ans1, ans2), i - l))
            ans1 = ans2
            l = i
    h_water_add = []
    for i, hw in enumerate(h_water_line):
        h_water_add.append(max(0, hw - h_tower[i]))
    return h_water_add

segment_tree = []

def build(v, tl, tr):
    tm = (tl + tr) // 2
    build(v * 2, tl, tm)
    build(v * 2 + 1, tm + 1, tr)

if __name__ == '__main__':
    f = open('h.txt', 'r')
    # h_tower = list(map(int, sys.stdin.readline().split()))
    h_tower = list(map(int, f.readline().split()))
    h_water = count_water(h_tower)
    app = QtWidgets.QApplication(sys.argv)
    windows = MyWidget(h_tower, h_water)
    windows.show()
    sys.exit(app.exec_())

