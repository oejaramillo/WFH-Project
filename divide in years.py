import pandas as pd

file_path = '_tempavisos.dta'

chunk_size = 10000
chunks = pd.read_stata(file_path, chunksize=chunk_size)

data = pd.DataFrame()

for chunk in chunks:
    data = pd.concat([data, chunk], ignore_index=True)


d2008 = data.loc[data['avisofechapublicacion'].dt.year == 2008]
d2009 = data.loc[data['avisofechapublicacion'].dt.year == 2009]
d2010 = data.loc[data['avisofechapublicacion'].dt.year == 2010]
d2011 = data.loc[data['avisofechapublicacion'].dt.year == 2011]
d2012 = data.loc[data['avisofechapublicacion'].dt.year == 2012]
d2013 = data.loc[data['avisofechapublicacion'].dt.year == 2013]
d2014 = data.loc[data['avisofechapublicacion'].dt.year == 2014]
d2015 = data.loc[data['avisofechapublicacion'].dt.year == 2015]
d2016 = data.loc[data['avisofechapublicacion'].dt.year == 2016]
d2017 = data.loc[data['avisofechapublicacion'].dt.year == 2017]
d2018 = data.loc[data['avisofechapublicacion'].dt.year == 2018]
d2019 = data.loc[data['avisofechapublicacion'].dt.year == 2019]
d2020 = data.loc[data['avisofechapublicacion'].dt.year == 2020]
d2021 = data.loc[data['avisofechapublicacion'].dt.year == 2021]
d2022 = data.loc[data['avisofechapublicacion'].dt.year == 2022]
d2023 = data.loc[data['avisofechapublicacion'].dt.year == 2023]

d2008.to_csv('datos\d2008.csv')
d2009.to_csv('datos\d2009.csv')
d2010.to_csv('datos\d2010.csv')
d2011.to_csv('datos\d2011.csv')
d2012.to_csv('datos\d2012.csv')
d2013.to_csv('datos\d2013.csv')
d2014.to_csv('datos\d2014.csv')
d2015.to_csv('datos\d2015.csv')
d2016.to_csv('datos\d2016.csv')
d2017.to_csv('datos\d2017.csv')
d2018.to_csv('datos\d2018.csv')
d2019.to_csv('datos\d2019.csv')
d2020.to_csv('datos\d2020.csv')
d2021.to_csv('datos\d2021.csv')
d2022.to_csv('datos\d2022.csv')
d2023.to_csv('datos\d2023.csv')