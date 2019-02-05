# Web-scraper-noDB

This crawler/scraper follows a depth first search algorithm to crawl the web pages. This depth can be specified by the user.

This program takes the URLs listed in the text file 'urllist.txt'. For each url, it checks the 'robot.txt' file and based on its rules, it parses the web pages. The user can introduce a manual delay of any number of seconds or allow the program to select a random delay between 1 and 10 seconds before each parse.

Algorithm:

Once the URL is selected from the 'urllist.txt' file, the program fetches all the other URLs existing on this homepage and stores them in the python dictionary. 

For each URL, it then parses content and metadata using 'urllib' and 'BeautifulSoup' libraries. Each word is converted to its stem and stored as a list of words in a document with a unique document ID. This unique ID is registered in the internal python dictionary and external dictionary file 'urllistDict.csv'. The documents are created in the 'Content' folder in the current directory.

-----------------------------

This program is limited to the Python dictionary size and can be used for academic projects without involving any database for managing/tracking URLs.

-----------------------------

It takes in the following parameters  -

<depth of the crawl> <delay (either 'r' or any number)> <'urllist.txt' path> <'urllistDict.csv' path>

** If delay is not entered as mentioned above, the program will continue with a delay of 0 seconds.