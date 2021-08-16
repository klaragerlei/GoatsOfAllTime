import numpy as np

def change_bin_size(array_in, window_size=10):
    array_with_different_bins = np.add.reduceat(array_in, range(0, len(array_in), window_size))
    return array_with_different_bins


def convert_data_to_bigger_bin_size_spikes(data_to_analyze, window=10):
    spikes_big_bins = []
    spikes_big_bins_original_shape = []
    for session_id, session in data_to_analyze.iterrows():
        spikes_in_session = []
        spikes_session_not_flat = []
        spikes = session.spikes
        for neuron in range(spikes.shape[0]):
            spikes_neuron = spikes[neuron]
            spikes_all_trials = np.array(spikes_neuron.reshape(-1))
            spikes_new_bin_size = change_bin_size(spikes_all_trials, window_size=window)
            spikes_in_session.append(spikes_new_bin_size)
            spikes_not_flat = spikes_new_bin_size.reshape(spikes_neuron.shape[0], int(spikes_neuron.shape[1]/window))
            spikes_session_not_flat.append(spikes_not_flat)
        spikes_big_bins.append(spikes_in_session)
        spikes_big_bins_original_shape.append(np.array(spikes_session_not_flat))
    data_to_analyze['spikes_bigger_bins'] = spikes_big_bins
    data_to_analyze['spikes_bigger_bins_not_flat'] = spikes_big_bins_original_shape
    print(data_to_analyze.spikes_bigger_bins)
    return data_to_analyze
