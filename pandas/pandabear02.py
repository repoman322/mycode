#!/usr/bin/python3
"""Alta3 Research | RZFeeser@alta3.com
   Challenge Soltuion - Exporting dataframe to different types"""


import pandas as pd

def main():
    # define the name of our xls file
    excel_file = 'movies.xls'

    # Choose the first column "Title" as
    # index (index=0)
    movies_sheet1 = pd.read_excel(excel_file, sheet_name=0, index_col=0)

    # grab the next 2 sheets as well
    movies_sheet2 = pd.read_excel(excel_file, sheet_name=1, index_col=0)

    movies_sheet3 = pd.read_excel(excel_file, sheet_name=2, index_col=0)

    # combine all DFs into a single DF called movies
    movies = pd.concat([movies_sheet1, movies_sheet2, movies_sheet3])

    # this returns a dataframe, or None if .drop_duplicates(inplace=True)
    movies.drop_duplicates(inplace=True)

    # sort DataFrame based on Gross Earnings
    sorted_by_gross = movies.sort_values(["Gross Earnings"], ascending=False)

    # show all of the avail export options
    print(dir(sorted_by_gross))

    # dependencies for all format exports (and imports) avail @
    # https://pandas.pydata.org/pandas-docs/stable/getting_started/install.html#recommended-dependencies

    # return top 10 movies in EXCEL format
    sorted_by_gross.head(10).to_excel('top10movies.xls')
    sorted_by_gross.head(10).to_excel('top10movies.xlsx')

    # return top 10 movies in CSV format
    sorted_by_gross.head(10).to_csv("top10movies.csv")

    # return top 10 movies in JSON format
    sorted_by_gross.head(10).to_json("top10movies.json")

if __name__ == "__main__":
    main()

