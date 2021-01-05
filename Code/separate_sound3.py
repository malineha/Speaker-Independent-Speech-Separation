from scipy.io import wavfile
from FastICA import FastICA
from FOBI import FOBI
import utilities as utl
import numpy as np


def separate_sound3(b,name):
	name=["1","2","3"]
	eps = 0.00000001
	
	#Read the mixed signals
	rate1, data1 = wavfile.read(b[0])
	rate2, data2 = wavfile.read(b[1])
	rate3, data3 = wavfile.read(b[2])

	#Centering the mixed signals and scaling the values as well
	data1 = data1 - np.mean(data1)
	data1 = data1/32768
	data2 = data2 - np.mean(data2)
	data2 = data2/32768
	data3 = data3 - np.mean(data3)
	data3 = data3/32768

	#Creating a matrix out of the signals
	signals = [data1, data2,data3]
	matrix = np.vstack(signals)

	#Whitening the matrix as a pre-processing step
	whiteMatrix = utl.whitenMatrix(matrix)

	X = whiteMatrix

	#Find the individual components one by one
	vectors = []
	for i in range(0, X.shape[0]):
		#The FastICA function is used as is from FastICA_image.py, and the it works out of the box
		vector = FastICA(X, vectors, eps)
		vectors.append(vector)

	#Stack the vectors to form the unmixing matrix
	W = np.vstack(vectors)

	#Get the original matrix
	S = np.dot(W, whiteMatrix)

	#Unmixing matrix through FOBI
	fobiW = FOBI(X)

	#Get the original matrix using fobiW
	fobiS = np.dot(fobiW.T, whiteMatrix)

	#Plot the separated sound signals
	utl.plotSounds([S[0], S[1], S[2]], ["1", "2", "3"], rate1, "separated")


	#Write the separated sound signals, 5000 is multiplied so that signal is audible
	wavfile.write("C:/SPEECH_SEPARATION--FinalYear/Separated/separate-" + name[0] + ".wav", rate1, 5000*S[0].astype(np.int16))
	wavfile.write("C:/SPEECH_SEPARATION--FinalYear/Separated/separate-" + name[1] + ".wav", rate1, 5000*S[1].astype(np.int16))
	wavfile.write("C:/SPEECH_SEPARATION--FinalYear/Separated/separate-" + name[2] + ".wav", rate1, 5000*S[2].astype(np.int16))


	#Plot the separated sound signals
	utl.plotSounds([fobiS[1], fobiS[0], fobiS[2]], ["1", "2", "3"], rate1, "separated_FOBI")

	#Write the separated sound signals, 5000 is multiplied so that signal is audible
	wavfile.write("C:/SPEECH_SEPARATION--FinalYear/Separated/separate-" + name[0] + ".wav", rate1, 5000*fobiS[1].astype(np.int16))
	wavfile.write("C:/SPEECH_SEPARATION--FinalYear/Separated/separate-" + name[1] + ".wav", rate1, 5000*fobiS[0].astype(np.int16))
	wavfile.write("C:/SPEECH_SEPARATION--FinalYear/Separated/separate-" + name[2] + ".wav", rate3, 5000*fobiS[2].astype(np.int16))