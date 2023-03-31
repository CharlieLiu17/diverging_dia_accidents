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

#I-15 & Timpanogos Highway
    # 40.431435, -111.890985
    # dd_filtered_df = precipitation_filtered_df.loc[(precipitation_filtered_df['Start_Lat'] < 40.431435 + .006)
    #                                                 & (precipitation_filtered_df['Start_Lat'] > 40.431435 - .006)
    #                                                 & (precipitation_filtered_df['Start_Lng'] < -111.890985 + .006)
    #                                                 & (precipitation_filtered_df['Start_Lng'] > -111.890985 - .006)]
    # dd_filtered_df.to_csv('dd_accidents/I15&Timpanogos.csv')

    # #SR-201 and Bangerter Highway
    # # 40.725842, -111.986348
    # dd_filtered_df = precipitation_filtered_df.loc[(precipitation_filtered_df['Start_Lat'] < 40.725842 + .006)
    #                                                 & (precipitation_filtered_df['Start_Lat'] > 40.725842 - .006)
    #                                                 & (precipitation_filtered_df['Start_Lng'] < -111.986348 + .006)
    #                                                 & (precipitation_filtered_df['Start_Lng'] > -111.986348 - .006)]
    # dd_filtered_df.to_csv('dd_accidents/SR201&Bangerter.csv')

# #I-435 and Front Street
# # 39.130039, -94.498942
# dd_filtered_df = precipitation_filtered_df.loc[(precipitation_filtered_df['Start_Lat'] < 39.130039 + .006)
#                                                 & (precipitation_filtered_df['Start_Lat'] > 39.130039 - .006)
#                                                 & (precipitation_filtered_df['Start_Lng'] < -94.498942 + .006)
#                                                 & (precipitation_filtered_df['Start_Lng'] > -94.498942 - .006)]
# dd_filtered_df.to_csv('dd_accidents/I435&FrontStreet.csv')

# #SR-201 and Bangerter Highway
#     # 40.725842, -111.986348
#     dd_filtered_df = precipitation_filtered_df.loc[(precipitation_filtered_df['Start_Lat'] < 40.725842 + .006)
#                                                     & (precipitation_filtered_df['Start_Lat'] > 40.725842 - .006)
#                                                     & (precipitation_filtered_df['Start_Lng'] < -111.986348 + .006)
#                                                     & (precipitation_filtered_df['Start_Lng'] > -111.986348 - .006)]
#     dd_filtered_df.to_csv('dd_accidents/SR201&Bangerter.csv')

    #MD295&ArundelMills
    # dd_filtered_df = precipitation_filtered_df.loc[((precipitation_filtered_df['Description'].str.lower().contains("arundel") == True)
    #                                                 | (precipitation_filtered_df['Street'].str.lower().contains("arundel") == True))]
    #                                                 #    & (precipitation_filtered_df['Street'].str.contains("I-44") == True)]
    # dd_filtered_df.to_csv('dd_accidents/test.csv')
    
    # dd_list[('I15', '500East')] = [40.360665, -111.785532]
    # dd_list[('US65', 'MO248')] = [36.657238, -93.221996]
    # dd_list[('I285', 'AshfordDunwoody')] = [33.918028, -84.338272]
    # dd_list[('MD295', 'ArundelMills')] = [39.156197, -76.745371]
    # dd_list[('US67', 'SR221')] = [37.771817, -90.445241]
    # dd_list[('I590','SouthWinton')] = [43.107697, -77.575899]
    # dd_list[('US65', 'ChestnutExpressway')] = [37.209615, -93.225983]

    # dd_list[('I580', 'MoanaLane')] = [39.492961, -119.784664]   
    # dd_list[('MO150', 'BottsRd')] = [38.858614, -94.546771]
    # dd_list[('I85', 'PleasantHillRd')] = [33.952269, -84.130002]
    # dd_list[('I44', 'RangeLineRd')] = [37.046582, -94.478628]
    # dd_list[('I44', 'RangeLineRd')] = [37.046582, -94.478628]
    # dd_list[('US60', 'SR13')] = [37.142496, -93.319401]
    # dd_list[('US52', 'OlmstedCountryRd')] = [44.183412, -92.576625]
    # dd_list[('I70', 'WoodsChapelRd')] = [39.034257, -94.305351]
    # dd_list[('I70', 'WoodsChapelRd')] = [39.034257, -94.305351]
    # dd_list[('I86', 'YellowstoneAve')] = [42.912826, -112.466349]
    # dd_list[('I35', 'HomesteadLane')] = [38.759334, -94.964149]
    # dd_list[('I70', 'StadiumBlvd')] = [38.968325, -92.371152]
    # dd_list[('I25', 'CollegeDrive')] = [41.099483, -104.850509]
    # dd_list[('SR15', 'SR120')] = [45.586444, -94.199452]
    # dd_list[('I270', 'RobertsRd')] = [40.002455, -83.118187]
    # dd_list[('I70', 'MidRiversMallDr')] = [38.799786, -90.620254]
    # dd_list[('I494', '34thAve')] = [44.862194, -93.223044]
    # dd_list[('I15', 'StGeorgeBlvd')] = [37.109781, -113.558017]
    # dd_list[('I64', 'US15')] = [37.977099, -78.213767]
    # dd_list[('I70', 'US50')] = [39.112223, -108.644204]
    # dd_list[('I77', 'CatawbaAve')] = [35.483539, -80.874847]

    # dd_list[('I29', 'TiffanySpringsPkwy')] = [39.273481, -94.669514] 
    # dd_list[('I15', 'UT130')] = [37.654484, -113.082340]
    # dd_list[('Loop375', 'Spur601')] = [31.841178, -106.324613]
    # dd_list[('I85', 'PoplarTentRd')] = [35.402011, -80.698395]
    # dd_list[('I15', 'US91')] = [41.485735, -112.053079]
    # dd_list[('I69', 'DuPontRd')] = [41.178894, -85.103439]
    # dd_list[('I85', 'NC73')] = [35.435306, -80.657534]
    # dd_list[('MN101', '141stAve')] = [45.210301, -93.552595]
    # dd_list[('I435', 'RoeAve')] = [38.932617, -94.639617]
    # dd_list[('I515', 'HorizonDr')] = [36.011847, -114.989998]
    # dd_list[('US65', 'Battlefield')] = [37.157972, -93.224452]
    # dd_list[('I85', 'JimmyCarterBlvd')] = [33.912092, -84.207853]
    # dd_list[('I485', 'MallardCreekRd')] = [35.362016, -80.749346]
    # dd_list[('I10', 'DIbervilleBlvd')] = [30.450806, -88.903791]
    # dd_list[('I15', 'UT68')] = [40.884232, -111.896639]
    # dd_list[('I40', 'SR66')] = [35.983616, -83.608209]
    # dd_list[('K10', 'RidgeviewRd')] = [38.941550, -94.797478]
    # dd_list[('I57', 'MorganAve')] = [37.744867, -88.956754]
    # dd_list[('I40', 'UnionCrossRd')] = [36.075110, -80.109677]
    # dd_list[('I88', 'SR59')] = [41.803683, -88.203734]
    # dd_list[('I95', 'US301')] = [34.670069, -79.005993]
    # dd_list[('US36', 'McCaslinBlvd')] = [39.957798, -105.165602]
    # dd_list[('I75', 'UniversityDr')] = [42.66577716126561, -83.24118370153525]
    # dd_list[('I35', 'CR96')] = [45.079172, -93.185617]
    # dd_list[('I26', 'AirportRd')] = [35.440453, -82.535744]
    # dd_list[('I35', 'UniversityBlvd')] = [30.558229, -97.69257]
    # dd_list[('I65', 'WorthsvilleRd')] = [39.587652, -86.063539]
    # dd_list[('I80', 'GrandPrairiePkwy')] = [41.569245, -93.853611]