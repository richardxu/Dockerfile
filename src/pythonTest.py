# Def
import numpy as np
import os
import time
from scipy.io.wavfile import read
from sklearn import preprocessing
import python_speech_features as mfcc
from sklearn.mixture import GMM # fit <frames,features> # <N,40>
from hmmlearn.hmm import GaussianHMM # fit <frames,features> # <M,40>


# recorder
import webrtcvad
vad = webrtcvad.Vad(3)
import wave
import pyaudio
from scipy.io import wavfile
FORMAT = pyaudio.paInt16
CHANNELS = 2
RATE = 8000
CHUNK_DURATION_MS = 30       # supports 10, 20 and 30 (ms)
CHUNK = int(RATE * CHUNK_DURATION_MS / 1000)  # chunk to read #CHUNK = 1024
audio = pyaudio.PyAudio()





print("Hello World !")






