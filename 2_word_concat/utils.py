import tensorflow as tf
from IPython.display import display, Audio
import numpy as np

def normalize(x):
    return (x - np.mean(x))/(np.std(x) + 1e-8)

def play(sound: np.ndarray, rate = 16000):
    display(Audio(sound, rate = rate))

def pad_audio_random(
    audio: np.ndarray, # audio sample to pad
    desired_length: int, # length of output audio
    start: int = 0, # padded output can only begin after index START
    end = None): # padded output must end before index END; end = desired_length by default

    if end == None:
        end = desired_length
    
    audio_len = audio.shape[0]
    assert end - start > audio_len, 'Must allow enough room in output array for sample audio!'
    begin_idx = np.random.randint(start, end-audio_len)
    out = np.concatenate([
        np.zeros(begin_idx), 
        audio, 
        np.zeros(desired_length - begin_idx - audio_len)
        ])
    return out

def generate_data(
    audio, 
    desired_length, 
    sample_size):

    data = []
    if type(audio) == tuple:
        audio1, audio2 = audio
        for _ in range(sample_size):
            len = desired_length // 2
            data.append(np.concatenate([pad_audio_random(audio1, len),
                                        pad_audio_random(audio2, len)]))
        return np.array(data)
    
    else:
        for _ in range(sample_size):
            data.append(pad_audio_random(audio, desired_length))
        return np.array(data)
    