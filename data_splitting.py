### split_data_to_training_and_test
def split_data_to_training_and_test(data_to_analyze, session_id=0, spikes_column_name='spikes'):
  X = data_to_analyze[spikes_column_name].iloc[session_id].transpose(2,1,0)
  # random_indices_test = random.choice(a, size=None, replace=True, p=None)
  # X: time bins by trials by neurons 
  # X: time bins by trials by neurons 
  print(X.shape)
  perm_idcs = np.random.permutation(X.shape[1])
  train_idx = round(0.8 * X.shape[1])
  X_train = X[:,perm_idcs[:train_idx]]
  X_test = X[:,perm_idcs[train_idx:]]
  print(X_train.shape)
  print(X_test.shape)
  return X_train, X_test
### Creates two copies of data for input and output. We don't need to do it like this, but this way we can change one of them if we want. 
def convert_for_network(session_data):
  x0 = torch.from_numpy(session_data).to(device).float()
  x1 = torch.from_numpy(session_data).to(device).float()
  return x0, x1

