import csv
import re


# CommentPreprocessing class for cleaning emojis and links from comments using regular expression
class CommentPreprocessing:
    def __init__(self, file_name, output_file_name):
        self.file_name = file_name  
        self.output_file_name = output_file_name

    # Function to remove emojis
    def remove_emojis(self,text):
        emoji_pattern = r"[^a-zA-Z0-9\s]+"
        return re.sub(emoji_pattern, "", text)

    # Function to remove links
    def remove_links(self,text):
        url_pattern = r"https?://\S+|www\.\S+"
        return re.sub(url_pattern, "", text)
    
    # Main function to clean emojis and links from comments
    def clean_comments(self):
        comments_file = open(self.file_name,"r" ,encoding="utf-8")
        cleaned_comments_file = open(self.output_file_name, "w", newline="")
        csv_reader = csv.reader(comments_file)
        csv_writer = csv.writer(cleaned_comments_file)
        for row in csv_reader:
            comment = row[0]  # Assuming comment is in the first column
            cleaned_comment = self.remove_emojis(self.remove_links(comment))
            csv_writer.writerow([cleaned_comment])

        # Close files
        comments_file.close()
        cleaned_comments_file.close()


