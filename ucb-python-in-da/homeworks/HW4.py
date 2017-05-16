from pylab import specgram, linspace
from matplotlib.pyplot import specgram
from scipy.io.wavfile import write
from scipy import sin, pi, int16

from module import plotMyWav # import plotMyWav function from module.py to plot vowel sounds

Fs=8000

# 2. Create a function that generates each simple formant tone with sampling frequency Fs=8kHz, duration 2 seconds, and different amplitudes based on the spectrograms of the American English Vowels provided by Ladeforged 2006:185-187.
# Refer to the spectrogram provided in the lectures and use your judgment. 
# Obtain best results by testing and repetition!
def vowel(fq1, fq2, fq3, amp1, amp2, amp3, Fs, length):
    t = linspace(0, length, length*Fs)
    sig = sin(2*pi*fq1*t)*amp1 + sin(2*pi*fq2*t)*amp2 + sin(2*pi*fq3*t)*amp3
    return sig.astype(int16)

# 1. Synthesize each formant tone in preparation for creating each vowel
# 3. Use the formant frequencies given by J.C. Wells - refer to the table provided in the lectures
I = vowel(360, 2220, 2960, 700, 700, 900, Fs, 2)
E = vowel(600, 2060, 2840, 900, 700, 700, Fs, 2 )
A = vowel(740, 1180, 2640, 1400, 1000, 500, Fs, 2)
OO = vowel(380, 940, 2300, 900, 600, 150, Fs, 2)
U = vowel(320, 920, 2200, 540, 320, 320, Fs, 2)


# 4. Simply add all three formants for each vowel and save the files in.wav format	
write('I.wav',Fs, I)
write('E.wav',Fs, E)
write('A.wav',Fs, A)
write('OO.wav',Fs, OO)
write('U.wav',Fs, U)


# 5. Extra point (optional): you can incorporate the code I provided in the previous slide as a module.py to plot each vowel sound. In this case send me both files.
plotMyWav('I.wav')
plotMyWav('E.wav')
plotMyWav('A.wav')
plotMyWav('OO.wav')
plotMyWav('U.wav')
