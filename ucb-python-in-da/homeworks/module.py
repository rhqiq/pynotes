## Visualiazing the power of frequency spectrum of a signal:
from pylab import linspace, subplot, plot, title, xlabel, ylabel, grid, axis, show
from numpy import arange, log10, sqrt, mean, sum
from scipy.io.wavfile import read
from scipy import fft, ceil

# 5. Extra point (optional): you can incorporate the code I provided in the previous slide as a module.py to plot each vowel sound. In this case send me both files.

def plotMyWav(filename):
    # We read the sound file of interest: 
    (Fs, x) = read(filename) # Fs - sampling frequency, x - signal
    
    # We create a windown for analysis, typecasting it to int (float will produce an error):
    win = int(Fs/4) 
    
    # We take the FFT with a specific window lenght: 
    x_fft = fft(x, win)
    
    # Now we obtain the magnitude of all frequencies in the signal using 'abs', 
    # then we scale by the number of signal points in order for the magnitude to be 
    # independent from the signal length 'len(x)', and finally we obtain the 
    # power of the signal by using '**2':
    sig_pow = ( abs(x_fft) / len(x) )**2 
    
    # We create an array containing the frequencies for the particular window used: 
    Freqs = arange(0, win, 2) * (Fs / win); 
    
    # Use only left side of the frequency power spectrum of the signal: 
    sig_pow = sig_pow[0:int(len(sig_pow)/2)] 
    
    # We plot the time-domain window of samples: 
    time = win/Fs # calculate the length of the .wav file in secs 
    t = linspace(0,time,win) # create evenly spaced numbers between [0:time]
    subplot(3,1,1), plot(t,x[0:win]) # plot signal 'x' 
    title('Sound plot of %s file' % filename) 
    xlabel('Time') 
    ylabel('Amplitude') 
    axis('tight') 
    grid(True) 
    
    # We scale the frequency array to [kHz] then plot the signal in dB by using 10*l og(10)p:
    subplot(3,1,3), plot(Freqs/win, 10*log10(sig_pow), color='r') 
    xlabel('Frequency (kHz)') 
    ylabel('Power (dB)') 
    axis('tight') 
    grid(True) 
    
    show()
