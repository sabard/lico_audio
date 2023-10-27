if len(midi_out) > 0:
    print(midi_out, flush=True)
for midi_event in midi_out:
    if midi_event[0] == 176:
        if midi_event[1] == 7: # volume
            amplitude = 1000. * midi_event[2] / 127.
        elif midi_event[1] == 1: # modulation
            pass # TODO implement LFO
    elif midi_event[0] != 0:
        key = midi_event[1] - 8
        freq = 440. * np.power(2, (key-49)/12.)
        if midi_event[0] == 144:
            keys_pressed[key] = freq
        elif midi_event[0] == 128:
            if key in keys_pressed.keys():
                del keys_pressed[key]

if len(keys_pressed) == 0:
    res = zeros
else:
    freqs = keys_pressed.values()
    res = np.sum(
        [synth.wave(2 * np.pi * freq * counter_interleaved) for freq in freqs], axis=0
    )[:]

if not stereo_out[0]:
    for i in range(res.size):
        if i % 2 == 0:  # 0 for left
            res[i] = 0

if not stereo_out[1]:
    for i in range(res.size):
        if i % 2 == 1:  # 1 for right
            res[i] = 0

sine_wave[:] = (res * amplitude).astype(np.int16)
counter_interleaved += timestep
