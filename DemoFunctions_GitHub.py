# -*- coding: utf-8 -*-
"""
Created on May 22nd 2018

DEMO FUNCTIONS

@author: rogers
"""

## Prompt user for basic details about the ranking so that we can include this information in the results/database

## APPEND METADATA FUNCTION -- for simple scraper
def DEMO_append_metadata(df, ranking_year, publication_date, ranking_scope, primary_ranking):
    df.insert(len(df.columns), 'Ranking Year', ranking_year)
    df.insert(len(df.columns), 'Publication Date', publication_date)
    df.insert(len(df.columns), 'Scope', ranking_scope)
    df.insert(len(df.columns), 'Primary Ranking', primary_ranking)
    return df

def DEMO_export_to_csv(df, ranking, ranking_year): 
    import os
    import pandas as pd

    #dir_name = 'C:\\Users\\rogers\\Desktop\\Demo_CSV_Files\\'
    dir_name = os.getcwd()
    base_filename ='DEMO_'+ ranking + '_' + str(ranking_year)
    suffix = '.csv'
    filename= os.path.join(dir_name, base_filename + suffix)

    
    print('Saving the data to csv...' )
    df.to_csv(filename, index=False)
