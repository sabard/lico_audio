import scipy
import numpy as np

# sampling_rate = 48000  # TODO make this available from config
sampling_rate = {{config["config"]["sampling_rate"]}}
timestep = 0.01
sig_len = int(timestep * sampling_rate * 2)
counter = (
    np.arange(timestep * sampling_rate).astype(np.float64) / sampling_rate
)
counter_interleaved = np.array(list(zip(counter, counter))).flatten()

zeros = np.zeros(sig_len)

stereo_out = (True, False)  # left/right

keys_pressed = {}

amplitude = 1000


def square_plus_saw(t):
    return np.sum(np.array([scipy.signal.square(t), scipy.signal.sawtooth(t)]), axis=0)


# signal_func = np.sin
# signal_func = scipy.signal.sawtooth
signal_func = scipy.signal.square
# signal_func = square_plus_saw


class Synth():

    def __init__(self, wave, unison=None, detune=None):
        if unison or detune:
            self.set_unison_detune(wave, unison, detune)
        else:
            self.wave = wave

    def set_unison_detune(self, wave, unison, detune):
        detune_freqs = np.linspace(1. - detune, 1. + detune, unison)
        waves = np.zeros((unison, sig_len))

        def new_wave(t):
            for i in range(unison):
                waves[i, :] = wave(t * detune_freqs[i])
            return np.sum(waves, axis=0)

        self.wave = new_wave


# synth = Synth(signal_func)
synth = Synth(signal_func, 13, 0.6)

tmp = synth.wave(zeros)
