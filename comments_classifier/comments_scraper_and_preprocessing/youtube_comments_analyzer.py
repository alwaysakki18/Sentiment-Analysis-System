# Import libraries for interacting with YouTube Data API and working with CSV files
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
import csv

class CommentScraper:
  """
  This class scrapes comments from a YouTube video and saves them to a CSV file.
  """
  def __init__(self, key):
    """
    Initializes the CommentScraper object with a developer key for the YouTube Data API.

    Args:
      key: A string containing your YouTube Data API developer key.
    """
    self.key = key
    self.yt_client = build(
      "youtube", "v3", developerKey=self.key
    )

  def get_comments(self, client, video_id, token=None):
    """
    Retrieves a list of comments for a given video ID using the YouTube Data API.

    Args:
      client: The YouTube Data API client object.
      video_id: The ID of the YouTube video for which to get comments.
      token: An optional page token to retrieve the next set of comments (pagination).

    Returns:
      A dictionary containing the retrieved comments or None on error.
    """
    try:
      response = (
        client.commentThreads()
          .list(
            part="snippet",
            videoId=video_id,
            textFormat="plainText",
            maxResults=100,
            pageToken=token,
          )
          .execute()
      )
      return response
    except HttpError as e:
      print(f"HTTP Error: {e.resp.status}")
      return None
    except Exception as e:
      print(f"An error occurred: {e}")
      return None

  def scrap_and_save(self, video_id, output_file_name):
    """
    Scrapes comments for a YouTube video and saves them to a CSV file.

    Args:
      video_id: The ID of the YouTube video for which to scrape comments.
      output_file_name: The name of the CSV file to save the comments to.
    """
    comments = []
    next_page_token = None

    while True:
      """
      Loop to retrieve comments in pages until all comments are retrieved.
      """
      resp = self.get_comments(self.yt_client, video_id, next_page_token)

      if not resp:
        break

      comments += resp["items"]
      next_page_token = resp.get("nextPageToken")
      if not next_page_token:
        break

    with open(output_file_name, "w", newline="", encoding="utf-8") as file:
      """
      Open the CSV file for writing and save comments as comma-separated values.
      """
      csv_writer = csv.writer(file)
      for comment in comments:
        comment_text = comment["snippet"]["topLevelComment"]["snippet"]["textDisplay"]
        csv_writer.writerow([comment_text])
