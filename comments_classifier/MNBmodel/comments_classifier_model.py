# Import necessary libraries
import os
import joblib

class ClassifierModel:
  """
  This class encapsulates a pre-trained Naive Bayes model for sentiment analysis.
  """

  def NBmodel():
    """
    Loads a pre-trained Naive Bayes model for sentiment analysis.

    Returns:
      The loaded Naive Bayes model.
    """

    return joblib.load(f"{os.getcwd()}/comments_classifier/MNBmodel/sentiment_analysis_model.joblib")
