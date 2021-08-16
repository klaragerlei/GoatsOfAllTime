### will not work as is, but don't need to fix it now. 
def reshape_pupil_data():
  # Make input features for model
  session_id = 0   # we will analyze this session
  session_to_analyze = data_to_analyze.spikes.iloc[session_id]
  print('number of spikes')
  print(data_to_analyze.number_of_spikes.iloc[session_id])
  print('Number of neurons in this session: ' + str(session_to_analyze.shape[0]))
  # try only one trial
  trial_id = 2
  session_to_analyze_reshaped = session_to_analyze[:,trial_id,:] # first trial 
  pupil_data = data_to_analyze.pupil.iloc[0][0,trial_id]  # first trial 

  print(session_to_analyze_reshaped.shape)
  print(pupil_data.shape)
