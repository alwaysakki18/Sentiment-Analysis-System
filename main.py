       #  IMPORTS         
import comments_classifier
import sys
import os
import csv
import numpy as np

        #  CHECKING IF THE CLI ARUGMENTS ARE CORRECT       
if len(sys.argv) != 2:
    print("Invalid arguments")
    sys.exit()

        #  FUNCTION TO READ AND CREATE LIST OF CLEANED DATA    
def create_list_of_comments(path):
    with open(path, 'r') as csvfile:  # Open the CSV file in read mode
        csv_reader = csv.reader(csvfile)  # Create a CSV reader object
        rows = list(csv_reader) # Read all rows into a list
    return rows

print("PROCESSING [1]....")

        #  GLOBAL VARIABLES        
video_id = sys.argv[1]
raw_file_name = f"{os.getcwd()}/comments_classifier/comments_scraper_and_preprocessing/output.csv"
preprocessed_file_name = f"{os
                            .getcwd()}/comments_classifier/comments_scraper_and_preprocessing/cleaned_comments.csv"

print("PROCESSING [2]....")
print("COLLECTING DATA....")

        #  SCRAPING COMMENTS FROM YOUTUBE, USING API       
scraper = comments_classifier.CommentScraper(key = "AIzaSyBh8drbZz_sSS-8tuSvldJOFZWZ7yLH9Y0")
scraper.scrap_and_save(video_id=video_id, output_file_name=raw_file_name)

print("DATA COLLECTED [3]....")
print("PROCESSING [4]....")

        #  PRE-PROCESSING COMMENTS (REMOVING EMOJIS AND LINKS)     
print("CLEANING DATA....")
comment_preprocessor = comments_classifier.CommentPreprocessing(raw_file_name,preprocessed_file_name)
comment_preprocessor.clean_comments()

print("DATA CLEANED [5]....")
print("MODEL PREPARING [6]....")

        #  SETTING UP MODEL FOR PREDICTIONS        
model = comments_classifier.ClassifierModel.NBmodel()

print("INITIALIZING TRANSFORMER [7]....")

    #  INITIALIZING TF-IDF TRANSFORMER
v = comments_classifier.TfidfTransformer.fit_transformer()

print("PRE-PROCESSING [8]....")

        #  CREATING LIST TO PASS FOR PREDICTION        
string_list = [i[0]  for i in create_list_of_comments(preprocessed_file_name) if len(i[0]) > 1]

print("PREDICTING THE REUSLTS [9]....")

    #  PREFORMING TRANSFORMATION AND PREDICTION        
comments_count = v.transform(string_list)
pred = model.predict(comments_count)

print("CALCULATING THE OUTPUT [10]....")

    #  PERFORMING AND PRINTING CALCULATIONS        
positive_per = (np.sum(pred)/len(pred))*100

print("\n----------------\n")
if positive_per >= 50:
    print("VIDEO HAS MORE POSITIVE COMMENTS!")
else:
    print("VIDEO HAS MORE NEGATIVE COMMENTS!")

print(f"THE POSITIVE PERCENTAGE IS : {positive_per}\nTHE NEGATIVE PERCENTAGE IS : {100-positive_per}")


