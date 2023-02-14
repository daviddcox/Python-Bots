#! /usr/bin/env python
######################################################################
# tuner.py - a minimal command-line guitar/ukulele tuner in Python.
# Requires numpy and pyaudio.
######################################################################
# Author:  Matt Zucker
# Date:    July 2016
# License: Creative Commons Attribution-ShareAlike 3.0
#          https://creativecommons.org/licenses/by-sa/3.0/us/
######################################################################

import numpy as np
import pyaudio


class Tuner:
    def __init__(self):
        ######################################################################
        # Feel free to play with these numbers. Might want to change NOTE_MIN
        # and NOTE_MAX especially for guitar/bass. Probably want to keep
        # FRAME_SIZE and FRAMES_PER_FFT to be powers of two.

        self.NOTE_MIN = 70       # C4
        self.NOTE_MAX = 100       # A4
        self.FSAMP = 22050       # Sampling frequency in Hz
        self.FRAME_SIZE = 1024   # How many samples per frame?
        self.FRAMES_PER_FFT = 16  # FFT takes average across how many frames?

        ######################################################################
        # Derived quantities from constants above. Note that as
        # SAMPLES_PER_FFT goes up, the frequency step size decreases (so
        # resolution increases); however, it will incur more delay to process
        # new sounds.

        self.SAMPLES_PER_FFT = self.FRAME_SIZE*self.FRAMES_PER_FFT
        self.FREQ_STEP = float(self.FSAMP)/self.SAMPLES_PER_FFT

        self.imin = max(0, int(np.floor(self.note_to_fftbin(self.NOTE_MIN - 1))))
        self.imax = min(self.SAMPLES_PER_FFT, int(np.ceil(self.note_to_fftbin(self.NOTE_MAX + 1))))

        # Allocate space to run an FFT.
        self.buf = np.zeros(self.SAMPLES_PER_FFT, dtype=np.float32)
        self.num_frames = 0

        # Initialize audio
        self.stream = pyaudio.PyAudio().open(format=pyaudio.paInt16,
                                        channels=1,
                                        rate=self.FSAMP,
                                        input=True,
                                        frames_per_buffer=self.FRAME_SIZE)



        # Print initial text
        print('sampling at', self.FSAMP, 'Hz with max resolution of', self.FREQ_STEP, 'Hz')

        ######################################################################
        # For printing out notes

        self.NOTE_NAMES = 'C C# D D# E F F# G G# A A# B'.split()

    ######################################################################
    # These three functions are based upon this very useful webpage:
    # https://newt.phys.unsw.edu.au/jw/notes.html

    def freq_to_number(self, f): return 69 + 12*np.log2(f/440.0)
    def number_to_freq(self, n): return 440 * 2.0**((n-69)/12.0)
    def note_name(self, n): return self.NOTE_NAMES[n % 12] + str(n/12 - 1)

    ######################################################################
    # Ok, ready to go now.

    # Get min/max index within FFT of notes we care about.
    # See docs for numpy.rfftfreq()
    def note_to_fftbin(self, n): return self.number_to_freq(n)/self.FREQ_STEP


    def run(self):
        # Create Hanning window function
        self.window = 0.5 * (1 - np.cos(np.linspace(0, 2 * np.pi, self.SAMPLES_PER_FFT, False)))
        self.stream.start_stream()
        # As long as we are getting data:
        counter = 0
        while self.stream.is_active():

            # Shift the buffer down and new data in
            self.buf[:-self.FRAME_SIZE] = self.buf[self.FRAME_SIZE:]
            self.buf[-self.FRAME_SIZE:] = np.fromstring(self.stream.read(self.FRAME_SIZE), np.int16)

            # Run the FFT on the windowed buffer
            fft = np.fft.rfft(self.buf * self.window)

            # Get frequency of maximum response in range
            freq = (np.abs(fft[self.imin:self.imax]).argmax() + self.imin) * self.FREQ_STEP

            # Get note number and nearest note
            n = self.freq_to_number(freq)
            n0 = int(round(n))

            # Console output once we have a full buffer
            self.num_frames += 1

            if self.num_frames >= self.FRAMES_PER_FFT:
                return freq
