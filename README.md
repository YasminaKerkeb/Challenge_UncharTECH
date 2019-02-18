# Challenge_UncharTECH
# Setting up the system : installing all the necessary packages
To use the script you need to install the nltk package. For Mac/Unix run on your terminal: '''sudo pip install -U nltk''' and for Windows run: pip install nltk

# About the script

The module regex is mainly used in the script. Basically we open the search Wikipedia URL, retrieve the first ten results, and extract the relevant content of each page. What may complicate things a bit is that there are some particular wikipedia search results (such as disambugation search pages where it is mentioned that the word we're looking for may refer to a lot of things, and other particlar pages where the content is basically a list (eg List of countries of oil production)). Therefore, Extracting the content differs from one type of page to another.

# Executing the script

To run the script, run  python Challenge.py on your terminal and the result for all pages is stored on Contenu_principal.txt. 

