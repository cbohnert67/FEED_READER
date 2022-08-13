# FEEDREADER

### Simple feed reader shell app that reads urls and displays feeds content. 

* The user can input one or several RSS feed URL.
* The reader will display the title, description, and link of the original content.

To run the app : 

python feedreader.py [OPTIONS] [URLS]

Options:
  * --top INTEGER  Top N entries that should be displayed for a feed. Must be used with only one url.
  * --title        Displays titles of all entries in each feed.
  * --all          Displays all entries in each feed.
  * --help         Show this message and exit.
