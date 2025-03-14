import numpy as np
import matplotlib.pyplot as plt
import wave
import numpy as np
import tqdm 



# x
with wave.open(r"./dataSource.wav") as f:
    metadata = f.getparams()
    frames = f.readframes(metadata.nframes)

print(metadata)
# print(frames)

pcm_samples = np.frombuffer(frames, dtype="<h")
normalized_amplitudes = pcm_samples / (2 ** 15)


# normalized_amplitudes = normalized_amplitudes[0:(*int(len(normalized_amplitudes)/10))]
dt = 1/metadata[2]
t_valsSource = np.linspace(0,len(normalized_amplitudes)*dt,len(normalized_amplitudes))


sourceData = normalized_amplitudes.copy()
# 1

with wave.open(r"./filter  1 One sycle.wav") as f:
    metadata = f.getparams()
    frames = f.readframes(metadata.nframes)

print(metadata)
# print(frames)

pcm_samples = np.frombuffer(frames, dtype="<h")
normalized_amplitudes = pcm_samples / (2 ** 15)


# normalized_amplitudes = normalized_amplitudes[0:(*int(len(normalized_amplitudes)/10))]
dt = 1/metadata[2]
t_valsFilter1 = np.linspace(0,len(normalized_amplitudes)*dt,len(normalized_amplitudes))


filter1Data = normalized_amplitudes.copy()

# 2

with wave.open(r"./filter  2OneSycle.wav") as f:
    metadata = f.getparams()
    frames = f.readframes(metadata.nframes)

print(metadata)
# print(frames)

pcm_samples = np.frombuffer(frames, dtype="<h")
normalized_amplitudes = pcm_samples / (2 ** 15)


# normalized_amplitudes = normalized_amplitudes[0:(*int(len(normalized_amplitudes)/10))]
dt = 1/metadata[2]
t_valsFilter2 = np.linspace(0,len(normalized_amplitudes)*dt,len(normalized_amplitudes))


filter2Data = normalized_amplitudes.copy()

##orginal
with wave.open(r"./orginalSoundOneSycle.wav") as f:
    metadata = f.getparams()
    frames = f.readframes(metadata.nframes)

print(metadata)
# print(frames)

pcm_samples = np.frombuffer(frames, dtype="<h")
normalized_amplitudes = pcm_samples / (2 ** 15)


# normalized_amplitudes = normalized_amplitudes[0:(*int(len(normalized_amplitudes)/10))]
dt = 1/metadata[2]
t_valsoriginal = np.linspace(0,len(normalized_amplitudes)*dt,len(normalized_amplitudes))


origonalData = normalized_amplitudes.copy()






def signal(amplitude:float, shift:float,freq:float,t_vals:np.ndarray[float],offset = 0)->np.ndarray[float]:
    """Generates datapoints for sinus signal

    Args:
        amplitude (float): Amplitude for signal
        shift (float): shit up and down vertical axsis
        freq (float): freqenci of signal
        t_vals (np.NDArray[float]): numpy array of evenly spaced t values
        offset () : offsets signal along the horizantal axsis

    Returns:
        numpy array contaning x(t)=A*sin(2pi*f*t)+c
    """
    return amplitude*np.sin(2*np.pi*freq*t_vals +offset)+shift
    #can 2 pi be pre calculated and is that faster? 

def exponetialPartFHat(freq:float,t_vals:np.ndarray[float])->np.ndarray[float]:
    """Returns real and imaginary part of exp(-2*pi*i*f*t) or exp(-w*t)

    Args:
        freq (float): frequancy
        t_vals (np.NDArray[float]): t values

    Returns:
        np.NDArray[float]: 2 d numpy array index 0 real part, index 1 imaginary part
    """
    negativ_angular_frequency_w = -2*np.pi*freq
    realPart = np.cos(t_vals*negativ_angular_frequency_w)
    imaginaryPart = np.sin(t_vals*negativ_angular_frequency_w)
    return np.array([realPart,imaginaryPart])

def f_hat_whole_freq(x_of_t, t_vals,scanRangeFreqMin,scanRangeFreqMax):
    """f hat or fourier transformation takes a signal x(t) and converts it to the freq domain

    Args:
        x_of_t (_type_): signal
        t_vals (_type_): time value
        scanRangeFreqMin (_type_): minimum freq
        scanRangeFreqMax (_type_): maximum freq

    Returns:
        _type_: index[0][0] real part of transformation, index[0][1] imaginary part of transformation, index[1] frqensy values
    """
    spectrumLen = scanRangeFreqMax-scanRangeFreqMin+1
    real_part = np.zeros(spectrumLen)
    imaginary_part = np.zeros(spectrumLen)
    freqencyValues = np.linspace(scanRangeFreqMin, scanRangeFreqMax, spectrumLen)
    print(freqencyValues)

    N = len(t_vals)
    for i in tqdm.trange(len(freqencyValues), desc="Processing"):
        freq = freqencyValues[i]
        exp_parts = exponetialPartFHat(freq, t_vals)  
        real_part[i] = np.sum( exp_parts[0] * x_of_t )/N
        imaginary_part[i] =np.sum( exp_parts[1] * x_of_t)/N
    
    return np.array([real_part, imaginary_part]), freqencyValues

        
def calculateMagnitude(forierValues):
    """Compines real and imaginary values from forirer transformation and adjust it to reflect amplitude of each signal

    Args:
        forierValues (_type_): 2d list with real and imagnery part at index 0 and 1 respecally

    Returns:
        _type_: 1d list with the combined values
    """
    return np.sqrt(forierValues[0]**2 + forierValues[1]**2)


def serchForFreq(fData,xdata,cutOffFromMax=0.5):
    """Serches for top points in data relative to the highest point in the data.

    Args:
        fData (_type_): freqency data
        xdata (_type_): amplitude data
        cutOffFromMax (float, optional): cutt of given in decimal value, higher value filters lower amplitude signals,lower values includes more signals but can include noise. Defaults to 0.5.

    Returns:
        _type_:List of freqcensies found
    """
    maxPoint = np.max(xdata)*cutOffFromMax
    topPointsFreq = []
    topPointsAmplitude = []
    for i in range(1, len(xdata) - 1):
        if (xdata[i]>xdata[i-1]) and (xdata[i]>xdata[i+1]) and (xdata[i]>maxPoint):
            topPointsFreq.append(fData[i])
            topPointsAmplitude.append(xdata[i])
    
    return np.array([topPointsFreq,topPointsAmplitude])


def createSignalFromFreq(freqencis,t_vals,ampltudes=[],offsetX=[],offsetY=[]):
    if len(ampltudes)==0:
        ampltudes = np.linspace(1,1,len(freqencis))
    
    if len(offsetX)==0:
        offsetX = np.zeros(len(freqencis))
    
    if len(offsetY)==0:
        offsetY = np.zeros(len(freqencis))
    
    combinedSignal = np.zeros(len(t_vals))
    for i in range(len(freqencis)):
        combinedSignal+=signal(ampltudes[i],offsetY[i],freqencis[i],t_vals,offsetX[i])
    return combinedSignal


def exponetialPartF(freq:float,t_vals:np.ndarray[float])->np.ndarray[float]:
    negativ_angular_frequency_w = 2*np.pi*freq
    realPart = np.cos(t_vals*negativ_angular_frequency_w)
    imaginaryPart = np.sin(t_vals*negativ_angular_frequency_w)
    return np.array([realPart,imaginaryPart])

def f(f_hat_values,freqencyValues,t_vals):
    f_values_real = np.zeros(len(t_vals))
    f_values_imaginary = np.zeros(len(t_vals))

    N = len(t_vals)

    for i in tqdm.trange(len(freqencyValues), desc="Processing"):
        freq = freqencyValues[i]
        exp_parts = exponetialPartF(freq, t_vals)  
        f_values_real += exp_parts[0] * f_hat_values[0][i]
        f_values_imaginary+= exp_parts[1] * f_hat_values[1][i]

    # f_values_real /= N
    # f_values_imaginary /=N
    return f_values_real,f_values_imaginary



def fToW(f):
    return f*2*np.pi

def bandStopSim(V_of_F,f,R,L,C):
    w = fToW(f)
    real =V_of_F[0]*(R/np.sqrt((R**2) + ((w*L)/(1-w**2 * L *C)**2)))
    img =V_of_F[1]*(R/np.sqrt((R**2) + ((w*L)/(1-w**2 * L *C)**2)))
    return np.array([real,img])



forierValuesSource,freqValuesSource = f_hat_whole_freq(sourceData,t_valsSource,0,3_000)
forierValuesFilter1,freqValuesFilter1 = f_hat_whole_freq(filter1Data,t_valsFilter1,0,3_000)
forierValuesFilte2,freqValuesFilter2 = f_hat_whole_freq(filter2Data,t_valsFilter2,0,3_000)
forierValuesoriginal,freqValuesoriginal = f_hat_whole_freq(origonalData,t_valsoriginal,0,3_000)

fourierMagnitudeDataSource = calculateMagnitude(forierValuesSource)
fourierMagnitudeDataFilter1= calculateMagnitude(forierValuesFilter1)
fourierMagnitudeDataFilte2 = calculateMagnitude(forierValuesFilte2)
fourierMagnitudeDataOriginal = calculateMagnitude(forierValuesoriginal)

np.savetxt('data.csv', np.column_stack((freqValuesSource, fourierMagnitudeDataSource, fourierMagnitudeDataFilter1, fourierMagnitudeDataFilte2,fourierMagnitudeDataOriginal)), 
           delimiter=',', fmt='%s', header="freqValuesSource,fourierValuesSource,fourierValuesFilter1,fourierValuesFilter2,original", comments='')

# plt.gca().set_yscale('log')
# plt.gca().set_xscale('log')
plt.title("Forier samlet, justert for magnitude")
plt.plot(freqValuesSource,fourierMagnitudeDataSource,color="blue",label="x(f)")
plt.plot(freqValuesFilter1,fourierMagnitudeDataFilter1,color="orange",label="y_1(f)")
plt.plot(freqValuesFilter2,fourierMagnitudeDataFilte2,color="green", label="y(f)/y_2(f)")
plt.grid()
plt.legend()
plt.axvline(color = "black")
plt.axhline(color = "black")
plt.show()
