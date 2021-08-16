# plot spikes across time
def plot_spikes_across_time(data_to_analyze,session_id=0,neuron_id=10):
  # spikes_of_neuron = data_to_analyze.spikes[session_id][neuron_id]

  session_to_analyze = data_to_analyze.spikes.iloc[session_id]
  number_of_spikes = data_to_analyze.number_of_spikes.iloc[session_id][neuron_id]
  print('Number of spikes: ' + str(number_of_spikes))
  spikes_of_neuron = session_to_analyze.reshape(session_to_analyze.shape[0], -1)[neuron_id]
  plt.figure()
  plt.plot(spikes_of_neuron)
  plt.show()
  plt.close()
  
  
# plot pupil size
def plot_pupil_size(data_to_analyze,session_id=0,neuron_id=10):
  print(data_to_analyze.iloc[session_id].pupil.shape)
  pupil_data_to_plot_1 = data_to_analyze.pupil.iloc[session_id][1].T[0]
  pupil_data_to_plot_2 = data_to_analyze.pupil.iloc[session_id][2].T[0]
  print(pupil_data_to_plot.shape)
  plt.figure()
  plt.plot(pupil_data_to_plot_1)
  plt.show()
  plt.close()
  plt.figure()
  plt.plot(pupil_data_to_plot_2)
  plt.show()
  plt.close()  
  
  
  
  
  
  
  
  
  
  
  
  
