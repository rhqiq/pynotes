# name: by Reza Haghighi
# Homework #4

from pylab import specgram, linspace
from matplotlib.pyplot import specgram
from scipy.io.wavfile import write
from scipy import sin, pi, int16
from module import vowel_plot


# 2. Create a function that generates each simple formant tone with sampling frequency Fs=8kHz, duration 2 seconds,
# and different amplitudes based on the spectrograms of the American English Vowels provided by Ladeforged 2006:185-187.
# Refer to the spectrogram provided in the lectures and use your judgment. 
# Obtain best results by testing and repetition!


def tone_gen(fq1, fq2, fq3, amp1, amp2, amp3, sound_len, fs=8000):
    t = linspace(0, sound_len, sound_len * fs)
    sig = sin(2 * pi * fq1 * t) * amp1 + sin(2 * pi * fq2 * t) * amp2 + sin(2 * pi * fq3 * t) * amp3
    return sig.astype(int16)


# 1. Synthesize each formant tone in preparation for creating each vowel
# 3. Use the formant frequencies given by J.C. Wells - refer to the table provided in the lectures
a = tone_gen(740, 1180, 2640, 1400, 1000, 500, 2)
e = tone_gen(600, 2060, 2840, 900, 700, 700, 2)
i = tone_gen(360, 2220, 2960, 700, 700, 900, 2)
o = tone_gen(380, 940, 2300, 900, 600, 150, 2)
u = tone_gen(320, 920, 2200, 540, 320, 320, 2)

# 4. Simply add all three formants for each vowel and save the files in.wav format
write('a.wav', 8000, a)
write('e.wav', 8000, e)
write('i.wav', 8000, i)
write('o.wav', 8000, o)
write('u.wav', 8000, u)

# 5. Extra point (optional): you can incorporate the code I provided in the previous slide as a module.py to plot each
# vowel sound. In this case send me both files.

vowel_plot('a.wav')
vowel_plot('e.wav')
vowel_plot('i.wav')
vowel_plot('o.wav')
vowel_plot('u.wav')
