### increase bin size for output. 

def convert_data_to_bigger_bin_size_face(data_to_analyze):
  face_data = []
  for session_id, session in data_to_analyze.iterrows():
    face_in_session = session.face
    face_data_flat = face_in_session.reshape(-1)
    face_new_bin_size = change_bin_size(face_data_flat, window_size=10)
    face_data.append(face_new_bin_size)
  data_to_analyze['face_bigger_bins'] = face_data
  return data_to_analyze

data_to_analyze = convert_data_to_bigger_bin_size_face(data_to_analyze) ### need to confirm this is the correct output. 

### increase bin size for spikes. 

def add_number_of_spikes_per_neuron_to_df(df):
  number_of_spikes = []
  for recording_index, recording in df.iterrows():
    spikes_all = recording.spikes
    spikes_neuron = []
    for neuron in range(spikes_all.shape[0]):
      num_of_spikes = np.sum(spikes_all[neuron])
      spikes_neuron.append(num_of_spikes)
    number_of_spikes.append(spikes_neuron)
  df['number_of_spikes'] = number_of_spikes
  return df      

data_to_analyze = add_number_of_spikes_per_neuron_to_df(data_to_analyze)
