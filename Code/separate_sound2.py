from scipy.io import wavfile
from FastICA import FastICA
from FOBI import FOBI
import utilities as utl
import numpy as np


def separate_sound2(b,name):
    #specifing epsilon(upper bound to the error)
    eps = 0.00000001
    
    # Read the mixed signals
    rate1, data1 = wavfile.read(b[0])
    rate2, data2 = wavfile.read(b[1])

    # Centering the mixed signals and scaling the values as well
    data1 = data1 - np.mean(data1)
    data1 = data1/32768
    data2 = data2 - np.mean(data2)
    data2 = data2/32768

    # Creating a matrix out of the signals
    signals = [data1, data2]
    matrix = np.vstack(signals)

    # Whitening the matrix as a pre-processing step
    whiteMatrix = utl.whitenMatrix(matrix)

    X = whiteMatrix

    # Find the individual components one by one
    vectors = []
    for i in range(0, X.shape[0]):
       
        vector = FastICA(X, vectors, eps)
        vectors.append(vector)

    # Stack the vectors to form the unmixing matrix
    W = np.vstack(vectors)

    # Get the original matrix
    S = np.dot(W, whiteMatrix)

    # Unmixing matrix through FOBI
    fobiW = FOBI(X)

    # Get the original matrix using fobiW
    fobiS = np.dot(fobiW.T, whiteMatrix)

    # Plot the separated sound signals
    utl.plotSounds([S[0], S[1]], ["1", "2"], rate1, "Separated")

    # Write the separated sound signals, 5000 is multiplied so that signal is audible
    wavfile.write("C:/SPEECH_SEPARATION--FinalYear/Separated/separate-" + name[0] + ".wav", rate1, 5000*S[0].astype(np.int16))
    wavfile.write("C:/SPEECH_SEPARATION--FinalYear/Separated/separate-" + name[1] + ".wav", rate1, 5000*S[1].astype(np.int16))
    # Plot the separated sound signals
    utl.plotSounds([fobiS[1], fobiS[0]], ["1", "2"], rate1, "Separated_FOBI")
    # Write the separated sound signals, 5000 is multiplied so that signal is audible
    wavfile.write("C:/SPEECH_SEPARATION--FinalYear/Separated/separate-" + name[0] + ".wav", rate1, 5000*fobiS[1].astype(np.int16))
    wavfile.write("C:/SPEECH_SEPARATION--FinalYear/Separated/separate-" + name[1] + ".wav", rate1, 5000*fobiS[0].astype(np.int16))