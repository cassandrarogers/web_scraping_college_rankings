# Scraping College Rankings

# What the code does
The script will extract the data from the rankings website, save it as a pandas dataframe, and export the data as a csv file for further use.

At present, the code can be used to scrape data from:
- US News Best Colleges
- US News Graduate Schools
- US News Online Programs
- Forbes
- PayScale College Salary

# The files
1. A jupyter notebook that will nicely show the data in a pandas dataframe: DEMO Final-GitHub.ipynb
2. A .txt file with the commands needed to call the GetRankings function: Commands to Scrape Rankings
3. The main function used to gather the rankings data: GitHub_RankingsScraperShell.py
4. Two other functions used to append metadata and export a csv file: DemoFunctions_GitHub.py


# Using the code
I recommend installing anaconda and jupyter notebook.

For the selenium code to work you'll need to have chromedriver.exe on your machine - you can download this for free but ensure that your version of the chrome browser and chromedriver are compatible. You will need to update the file path for chromedriver in the script to match where it is stored on your computer. The line of code you will need to edit in the GitHub_RankingsScraperShell.py file is:
driver = webdriver.Chrome('C:/Users/rogers/chromedriver.exe')

US News: replace the url parameter with another US News rankings url to collect the data for that school. Note that the scripts are specific to the US News ranking type as the webpages each have different formatting. 

Forbes: the script currently uses set of hard-coded college names and URLs. These are defined in the GitHub_RankingsScraperShell.py file so you can edit these there as needed.

PayScale: the entire table of rankings will be captured so you don't need to specify a school or url, but you can limit the # of rows you want to capture (i.e. limit = 10 when calling the function)- the default number is 25 but the rankings themselves go beyond 1500 so I'd recommend providing some limit to reduce the time taken to run the script.

The GetRankings function will also take a number of other optional arguments:
 - ranking year (useful for when the named year of the ranking differs from the year in which it was published)
 - publication year
 - publication month
 - publication day
 - scope (national, international, regional or any other string)
 - primary ranking (I used this binary 0/1 flag to denote whether this is one of the main rankings we track)

