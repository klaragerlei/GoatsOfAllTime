import pandas as pd
import numpy as np


def assign_numbers_to_brain_areas(recording, brain_groups):
  # print('Areas in this recording:' + str(np.unique(recording['brain_area'])))
    nareas = len(brain_groups)
      NN = len(recording['brain_area']) # number of neurons
        barea = nareas * np.ones(NN, ) # last one is "other"
	  for area_id in range(nareas):
	      barea[np.isin(recording['brain_area'], brain_groups[area_id])] = area_id # assign a number to each region
	        return barea


		def get_firing_data_for_area(df_to_add_to, data, name_of_area, brain_groups):
		  index_corresponding_to_area = np.where(brain_groups == name_of_area)[0][0]
		    # print(index_corresponding_to_area)
		      spikes = []
		        for recording_id in range(len(data)):
			    recording = data[recording_id]
			        barea = assign_numbers_to_brain_areas(recording, brain_groups)
				    spikes_in_recording = recording['spks'][barea==index_corresponding_to_area]
				        # print(spikes_in_recording)
					    spikes.append(spikes_in_recording)
					      df_to_add_to['spikes'] = spikes
					        return df_to_add_to


						def load_behavioural_feature(df_to_add_to, data, column_name):
						  features = []
						    for recording_id in range(len(data)):  
						        recording_data = data[recording_id]  # this is just one recording
							    feature = recording_data[column_name]
							        features.append(feature)
								  df_to_add_to[column_name] = features
								    return df_to_add_to

								    def drop_sessions_with_no_spikes(data_to_analyze):
								      sessions_to_drop = []
								        for session_index, session in data_to_analyze.iterrows():
									    if len(session.spikes) == 0:
									          sessions_to_drop.append(session_index)
										    
										      data_to_analyze = data_to_analyze.drop(sessions_to_drop, axis=0)
										        return data_to_analyze


											# Load firing data and behavioural variable for a given area
											def load_data_for_model(brain_area, behavioural_feature, brain_groups):
											  alldat = get_alldat()
											    data_to_analyze = pd.DataFrame()  # make empty df
											      # add behavioural feature to df
											        data_to_analyze = load_behavioural_feature(data_to_analyze, alldat, behavioural_feature)
												  # add spikes to df
												    data_to_analyze = get_firing_data_for_area(data_to_analyze, alldat, brain_area, brain_groups)
												      return data_to_analyze


												      def load_data(alldat, brain_area='MOp', feature='face'):
												        brain_groups = np.array(["VISa", "VISam", "VISl", "VISp", "VISpm", "VISrl","CL", "LD", "LGd", "LH", "LP", "MD", "MG", "PO", "POL", "PT", "RT", "SPF", "TH", "VAL", "VPL", "VPM","CA", "CA1", "CA2", "CA3", "DG", "SUB", "POST","ACA", "AUD", "COA", "DP", "ILA", "MOp", "MOs", "OLF", "ORB", "ORBm", "PIR", "PL", "SSp", "SSs", "RSP","TT","APN", "IC", "MB", "MRN", "NB", "PAG", "RN", "SCs", "SCm", "SCig", "SCsg", "ZI","ACB", "CP", "GPe", "LS", "LSc", "LSr", "MS", "OT", "SNr", "SI","BLA", "BMA", "EP", "EPd", "MEA"])
													  data_to_analyze = load_data_for_model(brain_area=brain_area, behavioural_feature=feature, brain_groups=brain_groups)
													    # data_to_analyze = load_data_for_model(brain_area=brain_area, behavioural_feature=behavioural_feature, brain_groups=brain_groups)
													      data_to_analyze = drop_sessions_with_no_spikes(data_to_analyze)
													        # print(data_to_analyze.head())
														  return data_to_analyze


														  data_to_analyze = load_data(alldat)
