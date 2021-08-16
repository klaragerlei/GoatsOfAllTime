import numpy as np


def change_bin_size(array_in, window_size=10):
    array_with_different_bins = np.add.reduceat(array_in, range(0, len(array_in), window_size))
    return array_with_different_bins


def convert_data_to_bigger_bin_size_spikes(data_to_analyze, window=10):
    print('Change binning of spike data.')
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

### might not be solely bin size based? Might have to move this later

## reshape motion energy
  def reshape_face_data(data_to_analyze, session_id=0, trial_id=None, spikes_column_name='spikes'):
    # Make input features for model
    session_to_analyze = data_to_analyze[spikes_column_name].iloc[session_id]
    print('number of spikes')
    print(data_to_analyze.number_of_spikes.iloc[session_id])
    #print(session_to_analyze)
    print('Number of neurons in this session: ' + str(session_to_analyze.shape[0]))

    session_to_analyze_reshaped = session_to_analyze[-1] # all trials 
    face_data = data_to_analyze.face.iloc[session_id][0,-1]  # all trials

    if trial_id != None:
      session_to_analyze_reshaped = session_to_analyze[:,trial_id,:] # one trial 
      face_data = data_to_analyze.face.iloc[session_id][0,trial_id]  # one trial 


    #print(session_to_analyze_reshaped.shape)
    #print(face_data.shape)
    return face_data, session_to_analyze_reshaped

