import librosa

# Load the audio file
AUDIO_FILE = './20190404_AVeryOffensiveRomCom.wav'
samples, sample_rate = librosa.load(AUDIO_FILE, sr=None)

sgram = librosa.stft(samples)
#librosa.display.specshow(sgram)

# use the mel-scale instead of raw frequency
sgram_mag, _ = librosa.magphase(sgram)
mel_scale_sgram = librosa.feature.melspectrogram(S=sgram_mag, sr=sample_rate)
#librosa.display.specshow(mel_scale_sgram)

# use the decibel scale to get the final Mel Spectrogram
mel_sgram = librosa.amplitude_to_db(mel_scale_sgram, ref=np.min)
librosa.display.specshow(mel_sgram, sr=sample_rate, x_axis='time', y_axis='mel')

#plt.colorbar(format='%+2.0f dB')

print(type(mel_sgram), mel_sgram.shape)
print("done")