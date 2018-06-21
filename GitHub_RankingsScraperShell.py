# -*- coding: utf-8 -*-
"""
Created on Mon May 21 15:30:15 2018

Rankings Scraper Shell

@author: rogers
"""


def GetRankings(ranking, **kwargs):
    import pandas as pd
    import datetime
    from selenium import webdriver
    from selenium.webdriver.support.wait import WebDriverWait
    from itertools import islice
    import urllib.request as urllib2
    from bs4 import BeautifulSoup
    
    from DemoFunctions_GitHub import DEMO_append_metadata, DEMO_export_to_csv

    date = datetime.date.today()

    url = kwargs.get('url', None)
    ranking_year = kwargs.get('ranking_year', date.year)
    publication_year = kwargs.get('publication_year', date.year)
    publication_month = kwargs.get('publication_month', date.month)
    publication_day = kwargs.get('publication_day', date.day)
    ranking_scope = kwargs.get('ranking_scope', 'National')
    primary_ranking = kwargs.get('primary_ranking', 1)
    
    publication_date = datetime.date(month = int(publication_month), day = int(publication_day), year = int(publication_year))
  
    print('\n','Ranking Metadata: ', '\n\n' ,
      'Ranking Year: ', ranking_year,  '\n' , 
      'Publication Date: ', publication_date, '\n' , 
      'Scope: ', ranking_scope, '\n' ,
      'Primary: ', primary_ranking, '\n\n')
    
    print('Initiating web scraping...')        
    
    driver = webdriver.Chrome('C:/Users/rogers/chromedriver.exe')
    
    if ranking == "US_News_Best_Colleges":
        driver.switch_to_window(driver.current_window_handle)
        
        ##UNCOMMENT THIS SECTION TO LOGIN TO US NEWS COMPASS
        #driver.get("https://secure.usnews.com/member/login")
        #username = driver.find_element_by_xpath('//*[@id="username"]')
        #password = driver.find_element_by_xpath('//*[@id="password"]')
        
        # ENTER US NEWS COMPASS LOGIN DETAILS
        #username.send_keys('') #USERNAME
        #password.send_keys('') #PASSWORD
        
        #driver.find_element_by_xpath('//*[@id="login_form"]/input[3]').click()
        
        driver.get(str(url)) # navigate to the college profile
        
        college_name = driver.find_element_by_xpath('/html/body/div[2]/div/div/div[2]/div[3]/div/div[1]/div[2]/h1').text
        ul = driver.find_elements_by_xpath('//*[@id="content-main"]/div[1]/div[2]/ul')
        data =[]
        rank =[]
        rankname =[]
        college_list =[]
        for u in ul:
            data = u.text.splitlines()
        for d in data:
             if d.startswith('At'):
                 data.remove(d)
        for part in data:
            rankname.append('US News - ' + str(part.split('in', 1)[1]).strip(' \n#'))
            rank.append(str(part.split('in', 1)[0]).strip(' \n#'))
            college_list.append(college_name)
        print(college_name + '- Data captured successfully')                   
        driver.quit()

        df = pd.DataFrame(list(zip(rank, rankname, college_list)))
        df.columns = ['Rank', 'Ranking Name', 'School']
        #print(df.head())
        
        #append the metadata to the df
        df = DEMO_append_metadata(df, ranking_year, publication_date, ranking_scope, primary_ranking)

        ## export data to a csv
        DEMO_export_to_csv(df, ranking, ranking_year)


    if ranking == "US_News_Online_Programs":        
        
        ##UNCOMMENT THIS SECTION TO LOGIN TO US NEWS COMPASS
        #driver.get("https://secure.usnews.com/member/login")
        #username = driver.find_element_by_xpath('//*[@id="username"]')
        #password = driver.find_element_by_xpath('//*[@id="password"]')
        
        # ENTER US NEWS COMPASS LOGIN DETAILS
        #username.send_keys('') #USERNAME
        #password.send_keys('') #PASSWORD
        
        #driver.find_element_by_xpath('//*[@id="login_form"]/input[3]').click()

        data =[]
        Ranks =[]
        RankingName =[]
        college_list = []
            
        driver.get(url)
        li = driver.find_elements_by_xpath('//*[@id="content-main"]/div[1]/div[2]')
        
        for l in li:
            data = l.text.splitlines()
        data = [x for x in data if not x.startswith('Online Programs Rankings')]
        data = [item.replace('#', '') for item in data]
        Rank = [d.split(' in ')[:1] for d in data]
        RN = [d.split(' in ')[1:] for d in data]

        college_name1 = driver.find_element_by_xpath('/html/body/div[2]/div/div/div[1]/div[2]/div/div[1]/div[2]/h1').text
        college_name2 = driver.find_element_by_xpath('/html/body/div[2]/div/div/div[1]/div[2]/div/div[1]/div[2]/h1/span/a').text
        college_name = college_name1.replace(college_name2, '').rstrip()

        college_rep = [college_name] * len(Rank)
        
        for item in Rank:
            Ranks.append(str(item).strip("[").strip("]").strip("'"))
        for R in RN:
            RankingName.append('US News Online Programs - ' + str(R).strip("[").strip("]").strip("'").strip("\""))
        for college in college_rep:
            college_list.append(college)
        print(college_name, ' - Data captured successfully')
        
        driver.quit()
        
        df = pd.DataFrame(list(zip(Ranks, RankingName, college_list)))
        df.columns = ['Rank', 'Ranking Name', 'School']
        #print(df)
        
        #append the metadata to the df
        df = DEMO_append_metadata(df, ranking_year, publication_date, ranking_scope, primary_ranking)

        ## export data to a csv
        DEMO_export_to_csv(df, ranking, ranking_year)
        
    if ranking == "US_News_Graduate_Schools":        

        ##UNCOMMENT THIS SECTION TO LOGIN TO US NEWS COMPASS
        #driver.get("https://secure.usnews.com/member/login")
        #username = driver.find_element_by_xpath('//*[@id="username"]')
        #password = driver.find_element_by_xpath('//*[@id="password"]')
        
        # ENTER US NEWS COMPASS LOGIN DETAILS
        #username.send_keys('') #USERNAME
        #password.send_keys('') #PASSWORD
        
        #driver.find_element_by_xpath('//*[@id="login_form"]/input[3]').click()
        
        data =[]
        Ranks =[]
        RankingName =[]
        college_list = []
        
        driver.get(url)
        li = driver.find_elements_by_xpath('//*[@id="content"]/div[3]/div[2]/div/ul')

        for l in li:
            data = l.text.splitlines()
        data = [num for num in data if num != 'Tie']
        data = [item.replace('#', '') for item in data]
        Rank = data[::2]
        RN = data[1::2]


        college_name = driver.find_element_by_xpath('//*[@id="content"]/h1').text.rstrip()

        college_rep = [college_name] * len(Rank)
        
        for item in Rank:
            Ranks.append(item)
        for R in RN:
            RankingName.append('US News Graduate Schools - ' + str(R))
        for college in college_rep:
            college_list.append(college)
        print(college_name, '- Data captured successfully')
        
        driver.quit()
    
        df = pd.DataFrame(list(zip(Ranks, RankingName, college_list)))
        df.columns = ['Rank', 'Ranking Name', 'School']
    
        #print(df)
        
        #append the metadata to the df
        df = DEMO_append_metadata(df, ranking_year, publication_date, ranking_scope, primary_ranking)

        ## export data to a csv
        DEMO_export_to_csv(df, ranking, ranking_year)
        
        
        
    if ranking == 'PayScale_College_Salary_Report':
       
        # get arg for # of schools, or get top 25 schools by default
        limit = kwargs.get('limit', 25)
        
        driver.get('https://www.payscale.com/college-salary-report/bachelors')
        wait = WebDriverWait(driver, 20)
        
        element = driver.find_element_by_xpath('//*[@id="collegeSalaryReportContent"]/div/div/div[2]/div/div/div/div[2]/a')
        driver.execute_script("return arguments[0].scrollIntoView(0, document.documentElement.scrollHeight-10);", element)
        driver.find_element_by_xpath('//*[@id="collegeSalaryReportContent"]/div/div/div[2]/div/div/div/div[2]/a').click()
        wait
        print('Full List Loaded')
        
        data1 =[]
        
        trs = driver.find_elements_by_xpath('//*[@id="collegeSalaryReportContent"]/div/div/div[2]/div/div/table/tbody/tr')

        # get the visible rows
        for tr in islice(trs, limit):
            tds = tr.find_elements_by_tag_name('td')
            data = (list(filter(None, (td.text for td in tds))))
            data1.insert(len(data1),data)
            print(data[1] + ' - Data captured successfully')
            
        driver.quit()
        df = pd.DataFrame(data1)
        
        # drop duplicate column of school names
        df.drop([2], axis=1,inplace = True)

        #set the columns to the table header
        df.columns = ['Rank', 'School', 'School Type', 'Early Career Pay','Mid-Career Pay', '% High Meaning','% STEM Degrees']
        df.insert(1,'Ranking Name', 'PayScale - College Salary Report')
        #print(df)
        #append the metadata to the df
        df = DEMO_append_metadata(df, ranking_year, publication_date, ranking_scope, primary_ranking)

        ## export data to a csv
        DEMO_export_to_csv(df, ranking, ranking_year)
        
        

        
    if ranking == 'Forbes': 
          ## ENTER COLLEGE NAMES HERE
        colleges = ['Illinois Institute of Technology',
                    'Colorado School of Mines',
                    'Case Western Reserve University',
                    'Northeastern University',
                    'New Jersey Institute of Technology',
                    'University of Texas at Dallas',
                    'University of Maryland, Baltimore County',
                    'Missouri University of Science and Technology',
                    'Michigan Technological University',
                    'New Mexico Institute of Mining and Technology',
                    'University of Massachusetts Lowell',
                    'Louisiana Tech University',
                    'Massachusetts Institute of Technology',
                    'California Institute of Technology',
                    'Carnegie Mellon University',
                    'Rensselaer Polytechnic Institute',
                    'Georgia Institute of Technology',
                    'Virginia Tech',
                    'Texas Tech University',
                    'Princeton University',
                    'The College of New Jersey',
                    'Rutgers University-New Brunswick',
                    'Stevens Institute of Technology',
                    'Montclair State University',
                    'Seton Hall University',
                    'Rowan University'
                    ]
        
        ## ENTER URLS TO CAPTURE HERE
        urls =['https://www.forbes.com/colleges/illinois-institute-of-technology/',
               'https://www.forbes.com/colleges/colorado-school-of-mines/',
               'https://www.forbes.com/colleges/case-western-reserve-university/',
               'https://www.forbes.com/colleges/northeastern-university/',
               'https://www.forbes.com/colleges/new-jersey-institute-of-technology/',
               'https://www.forbes.com/colleges/the-university-of-texas-at-dallas/',
               'https://www.forbes.com/colleges/university-of-maryland-baltimore-county/',
               'https://www.forbes.com/colleges/missouri-university-of-science-and-technology/',
               'https://www.forbes.com/colleges/michigan-technological-university/',
               'https://www.forbes.com/colleges/new-mexico-institute-of-mining-and-technology/',
               'https://www.forbes.com/colleges/university-of-massachusetts-lowell/',
               'https://www.forbes.com/colleges/louisiana-tech-university/',
               'https://www.forbes.com/colleges/massachusetts-institute-of-technology/',
               'https://www.forbes.com/colleges/california-institute-of-technology/',
               'https://www.forbes.com/colleges/carnegie-mellon-university/',
               'https://www.forbes.com/colleges/rensselaer-polytechnic-institute/',
               'https://www.forbes.com/colleges/georgia-institute-of-technology-main-campus/',
               'https://www.forbes.com/colleges/virginia-polytechnic-institute-and-state-university/',
               'https://www.forbes.com/colleges/texas-tech-university/',
               'https://www.forbes.com/colleges/princeton-university/',
               'https://www.forbes.com/colleges/the-college-of-new-jersey/',
               'https://www.forbes.com/colleges/rutgers-university-new-brunswick/',
               'https://www.forbes.com/colleges/stevens-institute-of-technology/',
               'https://www.forbes.com/colleges/montclair-state-university/',
               'https://www.forbes.com/colleges/seton-hall-university/',
               'https://www.forbes.com/colleges/rowan-university/'   
               ]
        
        rank =[]
        rankname =[]
        college_list =[]
        
        for idx, college in enumerate(colleges):
            page = urllib2.urlopen(urls[idx])
            
            tidy = BeautifulSoup(page, 'lxml')
            div = tidy.find('div', {'class':'forbeslists fright'})
            li = div.findAll('li')
            div1 = tidy.findAll('div', {'class':'rankonlist'})
            for d in div1:
                rankname.append('Forbes - ' + str(d.text.split(' ', 1)[1]).strip('\" \n'))
                rank.append(str(d.text.split(' ', 1)[0]).strip (' \n#'))
                college_list.append(colleges[idx])
            for l in li:
                    if ':' not in l.text:
                        rank.append(str(l.text.split('in')[0]).strip(' \n#'))
                        rankname.append('Forbes - ' + 'Top Colleges - ' + str(l.text.split('in')[1]).strip(' \n#'))
                        college_list.append(colleges[idx])
                    else:
                        rankname.append('Forbes - ' + str(l.text.split(':')[0]).strip('\" \n'))
                        rank.append(str(l.text.split(':')[1]).strip(' \n'))
                        college_list.append(colleges[idx])
            print(colleges[idx] + ' - Data captured successfully')
        
        df = pd.DataFrame(list(zip(rank, rankname, college_list)))
        df.columns = ['Rank', 'Ranking Name', 'School']
        #print(df)
        
        #append the metadata to the df
        df = DEMO_append_metadata(df, ranking_year, publication_date, ranking_scope, primary_ranking)
       

        ## export data to a csv
        DEMO_export_to_csv(df, ranking, ranking_year)
    return df;