from sqlalchemy import create_engine, func
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
import pandas as pd
import matplotlib.pyplot as plt
from config import info


#connect postgresql EPI data using sql alchemy
engine = create_engine(info)
Base = automap_base()
#load in data by connecting the engine to the automapper
Base.prepare(engine, reflect=True)


#connect corruption data
#import corruption data
corruption_df=pd.read_csv("/Users/Jackie/Desktop/GH_Clones/EPI_2010/corruption.csv")
#save as table
table_name="corruption_table"
corruption_df.to_sql(table_name, engine, if_exists='replace', index=False)

#Save tables as classes for EPI data
epi_country = Base.classes.epi_country
gdp = Base.classes.economic

session = Session(engine)
engine.dispose()

#select columns for analysis 
results_epi = session.query(epi_country.country, epi_country.air_h, epi_country.population07, epi_country.water_h, epi_country.biodiversity, epi_country.fisheries, epi_country.geo_subregion)
gdp_country = session.query(gdp.country, gdp.subject, gdp.value)

#save as rows
rows_epi = results_epi.all()
rows_gdp = gdp_country.all()

#save into dataframes
gdp_df = pd.DataFrame(rows_gdp, columns=['country', 'subject', 'value'])
epi_df = pd.DataFrame(results_epi, columns=['country', 'air_h', 'population07', 'water_h', 'biodiversity', 'fisheries','geo_subregion'])

#merge dfs on "country"
gdp_epi = gdp_df.merge(epi_df, how="left", on="country")

#some data exploration and dropna
#print(gdp_epi.isna().sum())
#print(gdp_epi.info())
clean_gdp_epi=gdp_epi.dropna()
#print(clean_gdp_epi.isna().sum())
#print(clean_gdp_epi["geo_subregion"].unique())


#data exploration for corruption data
#print(corruption_df.info())
#print(corruption_df.head())

#filter for South America region
epi_sa = clean_gdp_epi[clean_gdp_epi["geo_subregion"] == "South America"]
#merge filtered data with courrption data on country
sa_corruption=epi_sa.merge(corruption_df, how="left", on="country")


sa_corruption.plot.scatter(x="country",y="score",c="DarkBlue")



