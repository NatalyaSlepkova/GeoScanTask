import sys
from visualization import MyWidget
from PyQt5 import QtWidgets


def get_partial_max(h):  # getting the maximum array on prefixes and suffixes
    ans = [h[0]]
    for cur_h in h[1:]:
        ans.append(max(ans[-1], cur_h))
    return ans


def get_water_height_segment(l, r, h):  # getting the height of water above each tower in a given segment
    segm_h = h[l:r + 1]
    max_pref = get_partial_max(segm_h)
    segm_h.reverse()
    max_suff = get_partial_max(segm_h)
    max_suff.reverse()
    segm_h.reverse()
    ans = [0]
    for i in range(1, len(segm_h) - 1):
        ans.append(max(segm_h[i], min(max_pref[i - 1], max_suff[i + 1])) - segm_h[i])
    if len(segm_h) > 1:
        ans.append(0)
    return ans


def get_water_height(h_tower):  # getting the height of water above each tower
    cur_pos = 0
    h_water = []
    for i, h in enumerate(h_tower):  # splitting into segments without zeros
        if h == 0 or i == len(h_tower) - 1:
            l = get_water_height_segment(cur_pos, i, h_tower)
            h_water.extend(l)
            cur_pos = i + 1
    return h_water


if __name__ == '__main__':
    f = open('h.txt', 'r')
    # h_tower = list(map(int, sys.stdin.readline().split()))
    h_tower = list(map(int, f.readline().split()))
    h_water = get_water_height(h_tower)
    print(h_water)
    app = QtWidgets.QApplication(sys.argv)
    windows = MyWidget(h_tower, h_water)
    windows.show()
    sys.exit(app.exec_())

