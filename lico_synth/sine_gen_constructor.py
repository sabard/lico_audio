# sampling_rate = 48000  # TODO make this available from config
sampling_rate = {{config["config"]["sampling_rate"]}}
timestep = 0.01
counter = (
    np.arange(timestep * sampling_rate).astype(np.float64) / sampling_rate
)
counter_interleaved = np.array(list(zip(counter, counter))).flatten()

zeros = np.zeros(960)

stereo_out = (True, False)  # left/right

keys_pressed = {}
