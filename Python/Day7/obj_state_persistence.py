import os
import pickle


class ExperimentSnapshot:

  def __init__(
      self, experiment_id, model_type, hyperparameters, metrics, timestamp
  ):
    self.experiment_id = experiment_id
    self.model_type = model_type
    self.hyperparameters = hyperparameters
    self.metrics = metrics
    self.timestamp = timestamp

  def get_best_metric(self, metric_name):

    return self.metrics.get(metric_name)


def save_experiment(snapshot, file_path):

  with open(file_path, mode="wb") as file:
    pickle.dump(snapshot, file)


def load_experiment(file_path):

  if not os.path.exists(file_path):
    raise FileNotFoundError(f"The file at '{file_path}' does not exist.")


  with open(file_path, mode="rb") as file:
    return pickle.load(file)