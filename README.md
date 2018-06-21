# Rankings

For the selenium code to work you'll need to have chromedriver.exe on your machine - you can download this for free but ensure that your version of the chrome browser and chromedriver are compatible. You will need to update the file path for chromedriver in the script to match where it is stored on your computer. The line of code you will need to edit in the GitHub_RankingsScraperShell.py file is:
driver = webdriver.Chrome('C:/Users/rogers/chromedriver.exe')

US News: replace the url parameter with another US News rankings url to collect the data for that school. Note that the scripts are specific to the US News ranking type as the webpages each have different formatting. 

Forbes: the script currently uses set of hard-coded college names and URLs. These are defined in the GitHub_RankingsScraperShell.py file so you can edit these there as needed.

PayScale: the entire table of rankings will be captured so you don't need to specify a school or url, but you can limit the # of rows you want to capture (i.e. limit = 10 when calling the function)- the default number is 25 but the rankings themselves go beyond 1500 so I'd recommend providing some limit to reduce the time taken to run the script.

## PLANNED CHANGES/UPDATES
Add list of requirements

Allow the url argument to take either a single URL or a list of URLs

Autodectection of the ranking based on the URL itself to remove the need to specify the ranking when calling the function

Create a file to store the login credentials for US News Compass and let the main script check for these credentials
