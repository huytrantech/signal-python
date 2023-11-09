from scipy.io import wavfile
import matplotlib.pyplot as plt
import numpy as np
import simpleaudio as sa
import librosa
def read_and_play_wav(file_path):
    # Đọc file âm thanh WAV
    sample_rate, audio_data = wavfile.read(file_path)

    # Phát âm thanh
    # play_audio(audio_data, sample_rate)

    # Vẽ tín hiệu trong miền thời gian
    plot_time_domain(audio_data, sample_rate)

    # Biến đổi Fourier và vẽ tín hiệu trong miền tần số
    plot_frequency_domain(audio_data, sample_rate)

    # Biến đổi STFT và vẽ tín hiệu trong miền tần số
    plot_frequency_domain_stft(audio_data, sample_rate)

def play_audio(audio_data, sample_rate):
    # Phát âm thanh
    wave_obj = sa.WaveObject(audio_data, num_channels=1, sample_rate=sample_rate)
    play_obj = wave_obj.play()
    play_obj.wait_done()

def plot_time_domain(audio_data, sample_rate):
    # Vẽ biểu đồ trong miền thời gian
    time = np.arange(0, len(audio_data)) / sample_rate
    plt.figure(figsize=(12, 4))
    plt.plot(time, audio_data, color='blue')
    plt.title('Audio Signal in Time Domain')
    plt.xlabel('Time (s)')
    plt.ylabel('Amplitude')
    plt.show()

def plot_frequency_domain(audio_data, sample_rate):
    # Biến đổi Fourier
    fft_result = np.fft.fft(audio_data)
    fft_freq = np.fft.fftfreq(len(fft_result), d=1/sample_rate)

    # Vẽ biểu đồ trong miền tần số
    plt.figure(figsize=(12, 4))
    plt.plot(fft_freq, np.abs(fft_result), color='green')
    plt.title('Audio Signal in Frequency Domain')
    plt.xlabel('Frequency (Hz)')
    plt.ylabel('Amplitude')
    plt.show()

def plot_frequency_domain_stft(audio_data, sample_rate):
    # Biến đổi STFT
    stft_result = librosa.stft(audio_data)
    # D = librosa.amplitude_to_db(np.abs(stft_result), ref=np.max)
    #
    # # Vẽ biểu đồ trong miền tần số từ STFT
    # plt.figure(figsize=(12, 4))
    # librosa.display.specshow(D, sr=sample_rate, x_axis='time', y_axis='log')
    # plt.colorbar(format='%+2.0f dB')
    # plt.title('Audio Signal in Frequency Domain (STFT)')
    # plt.show()

if __name__ == "__main__":
    # Thay đổi đường dẫn thành đường dẫn của file WAV bạn muốn xử lý
    file_path = 'Dang Van Ngu.wav'
    read_and_play_wav(file_path)
