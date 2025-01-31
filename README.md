<h2>Title: Sentiment Analysis System (Accuracy: 86%)</h2>

<h2>Description:</h2>

This Python project implements sentiment analysis to determine the overall sentiment (positive, negative, or neutral)
of comments on a YouTube video. It leverages the power of a Naive Bayes Multinomial model, trained on the well-established 
IMDB 50k movie reviews dataset from Kaggle. The model boasts an impressive 86% accuracy on a 20% testing data split.

<h3>Key Features:</h3>

Sentiment Classification: Analyzes YouTube video comments and categorizes them as positive, negative, or neutral.

Naive Bayes Multinomial Model: Employs a powerful and efficient machine learning algorithm for sentiment analysis.

IMDB 50k Movie Reviews Dataset: Utilizes a high-quality and widely used dataset for effective model training.

86% Accuracy: Delivers reliable results on unseen YouTube video comments.

Easy to Use: Run the main.py script with a YouTube video ID to get started.

Requirements:

Python 3.x (with necessary libraries: googleapiclient, joblib, scikit-learn, etc.)
YouTube Data API v3 developer key (obtain one from https://console.developers.google.com/project)
Getting Started:

1.  Install Dependencies: Use pip install <library_name> for each required library (e.g., pip install googleapiclient).
2.  Obtain YouTube Data API Key: Create a project in the Google Cloud Platform Console, enable the YouTube Data API v3, and generate an API key.
3.  Place API Key: In your code (likely main.py), add your API key to the appropriate variable.
4.  Run the Script: Execute python main.py <video_id> (replace <video_id> with the actual YouTube video ID).


<h3>Bash</h3>
<h4>
python main.py "Video ID"  # Example YouTube video ID
</h4>




