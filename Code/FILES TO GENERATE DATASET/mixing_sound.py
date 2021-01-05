import utilities as utl
from scipy.io import wavfile
import numpy as np

# Read the files as numpy array
rate1, data1 = wavfile.read("13-84-1.wav")
rate2, data2 = wavfile.read("13-172-1.wav")

# Using the mixSounds helper function from utilities.py
mixedX = utl.mixSounds([data1, data2], [0.3, 0.7]).astype(np.int16)
mixedY = utl.mixSounds([data1, data2], [0.6, 0.4]).astype(np.int16)

# Plot the mixed sound sources
utl.plotSounds([mixedX, mixedY], ["mixed-1","mixed-3"], rate1, "../plots/sounds/Ring_StarWars_mixed", False)

# Save the mixed sources as wav files
wavfile.write("mixed-1.wav", rate1, mixedX)
wavfile.write("mixed-3.wav", rate1, mixedY)
