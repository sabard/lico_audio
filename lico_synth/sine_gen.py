if midi_out[0] != 0:
    key = midi_out[1] - 20
    freq = 440. * np.power(2, (key-49)/12.)
    if midi_out[0] == 144:
        keys_pressed[key] = freq
    elif midi_out[0] == 128:
        del keys_pressed[key]

if len(keys_pressed) == 0:
    res = zeros
else:
    freqs = keys_pressed.values()
    res = np.sum(
        [np.sin(2 * np.pi * freq * counter_interleaved) for freq in freqs], axis=0
    )[:]

if not stereo_out[0]:
    for i in range(res.size):
        if i % 2 == 0:  # 0 for left
            res[i] = 0

if not stereo_out[1]:
    for i in range(res.size):
        if i % 2 == 1:  # 1 for right
            res[i] = 0

sine_wave[:] = (res * 1000).astype(np.int16)
counter_interleaved += timestep
