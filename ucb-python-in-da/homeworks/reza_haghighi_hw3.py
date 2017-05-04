# 1. Include a sec4on line with your name
# name: by Reza Haghighi

# 2. Work only with these imports
from numpy import matrix, array, random, min, max
import pylab as plb

# 3. Create a list A of 600 random numbers bound between (0:10)
# A = random.uniform(0, 10, size=600)
A = [random.uniform(0.1, 10) for _ in range(600)]


# 4. Create an array B with with 500 elements bound in the range [-3*pi:2*pi]
# B = random.uniform(-3 * plb.pi, 2 * plb.pi, size=500)
B = plb.linspace(-3 * plb.pi, 2 * plb.pi, 500, endpoint=True)

# 5. Using if, for or while, create a function that overwrites every element in A that falls outside of the interval
#    [2:9), and overwrite that element with the average between the smallest and largest element in A


def modify_list(l):
    for i in range(len(l)):
        if l[i] < 2 or l[i] >= 9:
            l[i] = (max(l) + min(l)) / 2
        # 6. Normalize each list element to be bound between [0:0.1] /A = [(x-min(A))/(10 * (max(A)-min(A))) for x in A]
        l[i] = (l[i] - min(A)) / (10 * (max(A) - min(A)))
    return l

# 7. Return the result from the function to C
C = modify_list(A)

# 8. Cast C as an array
C = array(C)

# 9. Add C to B (think of C as noise) and record the result in D
D = plb.resize(C, (500,)) + B

# 10. Create a figure, give it a title and specify your own size and dpi
fig = plb.figure(figsize=(10, 6), dpi=120).suptitle("Homework 3")


# 11. Plot the sin of D, in the (2,1,1) location of the figure
d_sin = plb.sin(D)
plb.subplot(2, 1, 1)
plb.plot(D, d_sin, color='red', linewidth=1, label='sin')


# 12. Overlay a plot of cos using D, with different color, thickness and type of line
d_cos = plb.cos(D)
plb.plot(D, d_cos, color='blue', linewidth=3, linestyle='-.', label='cos')

# 13. Create some space on top and bottom of the plot (on the y axis) and show the grid
plb.grid(True)
plb.ylim(-2.5, 2.5)

# 14. Specify the following: title, Y-axis label and legend to fit in the best way
plb.ylabel('Y Axis')
plb.title('d-sin & d-cos plot')
plb.legend(loc='upper right')

# 15. Plot the tan of D, in location (2,1,2) with grid showing, X-axis label, Y-axis label and legend on top right
d_tan = plb.tan(D)
plb.subplot(2, 1, 2)
plb.plot(D, d_tan, color='green', linewidth=2, label='tan')
plb.xlabel('X Axis')
plb.ylabel('Y Axis')
plb.legend(loc='upper right')
plb.show()
