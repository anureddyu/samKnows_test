#Use Pandas to create Dataframe on csv
import pandas as pd

#Create dataframe on measurements data
df = pd.read_csv('data_engineering.csv')

#case where both successes and failures are '1'  
df1 = df.query('successes == 1 & failures == 1')

# Using 'anomaly_desc' as the column name 
df1['anomaly_desc'] = 'both failures and successes are true'

#Finding duplicates (UUID processed at the same time)
df2=pd.concat(dup for _, dup in df.groupby(["measurement_datetime",'device_identifier']) if len(dup) > 1)

# Using 'anomaly_desc' as the column name 
df2['anomaly_desc'] = 'Duplicate records with same UUID and measurement_datetime'

#Failed even when all the data is processed(includes 0 byte files)
df3= df.query('(((bytes_per_second * fetch_time)/1000000)-10) <= bytes_total <= (((bytes_per_second * fetch_time)/1000000)+10)').query("successes == 0")

# Using 'anomaly_desc' as the column name 
df3['anomaly_desc'] = 'All the data has been processed but recorded as failure'

#Bytes per second has negative values
df4 = df.query('bytes_per_second < 0')

# Using 'anomaly_desc' as the column name 
df4['anomaly_desc'] = 'Bytes of data processed per second is recorded in negative values'

#Union/concat all the derived anomaly dataframes
anomalies_df = pd.concat([df1,df2,df3,df4])

#Load the anomalies into csv 
anomalies_df.to_csv('anamalies_csv.csv')
