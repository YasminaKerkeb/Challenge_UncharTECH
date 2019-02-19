# Challenge_UncharTECH
# Setting up the system : installing all the necessary packages
To use the script you need to install the nltk package. 
For Mac/Unix run on your terminal: 
```sudo pip install -U nltk ```
and for Windows: ``` run: pip install nltk ```

# About the script

The module regex is mainly used in the script. Basically we open the search Wikipedia URL, retrieve the first ten results, and extract the relevant content of each page. What may complicate things a bit is that there are some particular wikipedia search results (such as disambugation search pages where it is mentioned that the word we're looking for may refer to a lot of things, and other particlar pages where the content is basically a list (eg List of countries of oil production)). Therefore, Extracting the content differs from one type of page to another.

# Executing the script

To run the script, run ``` python Challenge.py ``` on your terminal and each result for a keyword is stored on ```keyword.txt```. 

Infos concerning my machine: 
```CPU 1,6 GHz Intel Core i5```

```RAM 4 Go 1600 MHz DDR3```

```APPLE SSD AP0256H```

Time indicator on my machine to execute the script: about 110 seconds

