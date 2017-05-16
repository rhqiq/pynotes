# name: by Reza Haghighi
# Homework #4

from pylab import linspace, subplot, plot, title, xlabel, ylabel, grid, axis, show
from numpy import arange, log10
from scipy.io.wavfile import read
from scipy import fft

# 5. Extra point (optional): you can incorporate the code I provided in the previous slide as a module.py
# to plot each vowel sound. In this case send me both files.


def vowel_plot(file):

    (Fs, x) = read(file)
    win = int(Fs/4)
    x_fft = fft(x, win)
    sig_pow = ( abs(x_fft) / len(x))**2

    Freqs = arange(0, win, 2) * (Fs / win)
    sig_pow = sig_pow[0:int(len(sig_pow)/2)]

    time = win/Fs
    t = linspace(0, time, win)
    subplot(3, 1, 1), plot(t, x[0:win])
    title('Sound plot of ' + file + ' file')
    xlabel('Time') 
    ylabel('Amplitude') 
    axis('tight') 
    grid(True) 

    subplot(3, 1, 3), plot(Freqs/win, 10*log10(sig_pow), color='r')
    xlabel('Fs (kHz)')
    ylabel('Power (dB)') 
    axis('tight') 
    grid(True) 
    
    show()
