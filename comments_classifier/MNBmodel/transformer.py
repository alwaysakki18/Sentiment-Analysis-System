# Import necessary libraries
import os
import joblib

class TfidfTransformer:
 """
 This class encapsulates a pre-trained TF-IDF transformer for text processing.
 """

 def fit_transformer():
   """
   Loads a pre-trained TF-IDF transformer model from a joblib file.

   Returns:
     The loaded TF-IDF transformer model.
   """

   return joblib.load(f"{os.getcwd()}/comments_classifier/MNBmodel/v_dump.joblib")

