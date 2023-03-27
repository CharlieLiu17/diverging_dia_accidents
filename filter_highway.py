import pandas as pd
#Open US Accidents data set
#Filter out all accidents that are not on a highway
#Save the filtered data set to a new file


def filter_highway():
    #Using file_read, filter by the column "Junction" and only keep the rows that have true in the column
    #Save the filtered data set to a new file
    #Open the file
    dd_list = [""]
    df = pd.read_csv('US_Accidents_Dec21_updated.csv',
                     usecols=['ID', 'Start_Lat', 'Start_Lng', 'Severity', 'Description', 'Street', 'Junction', 'State', 'Precipitation(in)', 'Weather_Condition'])
    junction_filtered_df = df[df['Junction'] == True]
    precipitation_filtered_df = junction_filtered_df[junction_filtered_df['Precipitation(in)'] >= 0]

    #I-15 & Timpanogos Highway
    # 40.431435, -111.890985
    dd_filtered_df = precipitation_filtered_df.loc[(precipitation_filtered_df['Start_Lat'] < 40.431435 + .006)
                                                    & (precipitation_filtered_df['Start_Lat'] > 40.431435 - .006)
                                                    & (precipitation_filtered_df['Start_Lng'] < -111.890985 + .006)
                                                    & (precipitation_filtered_df['Start_Lng'] > -111.890985 - .006)]
    dd_filtered_df.to_csv('dd_accidents/I435&FrontStreet.csv')
    
    return dd_filtered_df
    #Create a new file
    
if (__name__ == "__main__"):
    filtered_df = filter_highway()
    print(filtered_df)