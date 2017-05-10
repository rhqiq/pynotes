# name: Reza Haghighi

import numpy as np
import pylab as plb

A = np.arange(5, 29, step=2)


def sam(arr, win=2):
    ret = np.cumsum(arr)
    ret[win:] = ret[win:] - ret[:-win]
    return win, ret[win - 1:] / win

win1, B = sam(A)
win2, C = sam(A, 4)

print('The Original Array is: \n', A)
print('The SAM of A with default window width is: \n', B, ' & width1 is: ', win1)
print('The SAM of A with window width of 4 is: \n', C, ' & width2 is: ', win2)


fig = plb.figure(figsize=(10, 6), dpi=120).suptitle("Midterm")


B_sin = np.sin(B)
C_sin = np.sin(C)


plb.plot(B, B_sin, color='red', linewidth=2, linestyle='--', label='B_sin')
plb.plot(C, C_sin, color='blue', linewidth=2, linestyle='-.', label='C_sin')

plb.grid(True)
plb.legend(loc='upper right')
plb.xlim(4, 27)
plb.ylim(-1, 1.25)

plb.show()
