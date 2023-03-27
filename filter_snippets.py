#TEMPLATE
#dd_filtered_df = precipitation_filtered_df.loc[(precipitation_filtered_df['Description'].str.contains("I-270") == True)]
                                                #    & (precipitation_filtered_df['Street'].str.contains("I-44") == True)]
# dd_filtered_df.to_csv('test.csv')

#I44 and MO-13
# dd_filtered_df = precipitation_filtered_df.loc[(precipitation_filtered_df['Description'].str.contains("MO-13/") == True)
#                                                & (precipitation_filtered_df['Street'].str.contains("I-44") == True)]
# dd_filtered_df.to_csv('I44&MO13.csv')

#US-60 and National Ave
# dd_filtered_df = precipitation_filtered_df.loc[((precipitation_filtered_df['Street'].str.contains("James River Fwy") == True)
#                                                 & (precipitation_filtered_df['Description'].str.contains("National Ave") == True))
#                                                 | ((precipitation_filtered_df['Description'].str.contains("National Ave") == True)
#                                                 & (precipitation_filtered_df['Description'].str.contains("US-60") == True))]
# dd_filtered_df.to_csv('US60&NatAve.csv')

#I-270 and Dorsett
# dd_filtered_df = precipitation_filtered_df.loc[(precipitation_filtered_df['Description'].str.contains("Dorsett") == True)
#                                                    |  (precipitation_filtered_df['Description'].str.contains("DORSETT") == True)]
    
#     dd_filtered_df.to_csv('I270&Dorsett.csv')

#US 129 and Middlesettlements Road no results
# dd_filtered_df = precipitation_filtered_df.loc[(precipitation_filtered_df['Description'].str.contains("Middlesettlement") == True)]
#                                             #    | (precipitation_filtered_df['Street'].str.contains("Middlesettlement") == True)]
#                                                 #    & (precipitation_filtered_df['Street'].str.contains("I-44") == True)]
# dd_filtered_df.to_csv('US129&Middlesettlement.csv')

#I-15 and American Fork
# dd_filtered_df = precipitation_filtered_df.loc[((precipitation_filtered_df['Description'].str.contains("W Main St") == True)
#                                                 | (precipitation_filtered_df['Street'].str.contains("W Main St") == True))
#                                                 & (precipitation_filtered_df['State'].str.contains("UT") == True)]
#                                                 #    & (precipitation_filtered_df['Street'].str.contains("I-44") == True)]
# dd_filtered_df.to_csv('dd_accidents/I-15&AmericanFork.csv')

#KY 4 and US 68
#38.015650, -84.551279
# #38.015756, -84.548983
# #38.018660, -84.552125
# dd_filtered_df = precipitation_filtered_df.loc[(precipitation_filtered_df['Start_Lat'] < 38.015650 + .006)
#                                                 & (precipitation_filtered_df['Start_Lat'] > 38.015650 - .006)
#                                                 & (precipitation_filtered_df['State'].str.contains("KY") == True)]
#                                                 # & (precipitation_filtered_df['Start_Lng'] < -84.551279 + .003)
#                                                 # & (precipitation_filtered_df['Start_Lng'] > -84.551279 - .003)]
# dd_filtered_df.to_csv('dd_accidents/test.csv')


#I-435 & Front Street
    # 39.130078, -94.498982
    # dd_filtered_df = precipitation_filtered_df.loc[(precipitation_filtered_df['Start_Lat'] < 39.130078 + .006)
    #                                                 & (precipitation_filtered_df['Start_Lat'] > 39.130078 - .006)
    #                                                 & (precipitation_filtered_df['Start_Lng'] < -94.498982 + .006)
    #                                                 & (precipitation_filtered_df['Start_Lng'] > -94.498982 - .006)]
    # dd_filtered_df.to_csv('dd_accidents/I435&FrontStreet.csv')
