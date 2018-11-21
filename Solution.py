from itertools import repeat
import sys
from collections import deque
from visualization import MyWidget
from PyQt5 import QtWidgets


def get_water_line(l, r, climbs):
    ans = []
    dq = deque([(0, l)])
    for (h, i) in climbs:
        while len(dq) >= 2:
            if dq[-1][0] < dq[-2][0] and dq[-1][0] < h:
                dq.pop()
            else:
                break
        dq.append((h, i))
    dq.append((0, r))
    for i in range(1, len(dq)):
        ans.extend(repeat(min(dq[i - 1][0], dq[i][0]), dq[i][1] - dq[i - 1][1]))
    ans.append(0)
    return ans


def count_water(h_tower):
    climbs = []
    h_tower = [0] + h_tower
    h_tower.append(0)
    water_line = []
    cur_pos = 1
    for i in range(1, len(h_tower) - 1):
        if h_tower[i] > h_tower[i - 1] and h_tower[i] > h_tower[i + 1]:
            climbs.append((h_tower[i], i))
        if h_tower[i] == 0:
            l = get_water_line(cur_pos, i, climbs)
            water_line.extend(l)
            climbs = []
            cur_pos = i + 1

    l = get_water_line(cur_pos, len(h_tower) - 2, climbs)
    water_line.extend(l)
    h_water_add = []
    for i, hw in enumerate(water_line):
        h_water_add.append(max(0, hw - h_tower[i + 1]))
    return h_water_add


if __name__ == '__main__':
    f = open('h.txt', 'r')
    # h_tower = list(map(int, sys.stdin.readline().split()))
    h_tower = list(map(int, f.readline().split()))
    h_water = count_water(h_tower)
    print(h_water)
    app = QtWidgets.QApplication(sys.argv)
    windows = MyWidget(h_tower, h_water)
    windows.show()
    sys.exit(app.exec_())

