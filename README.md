# samKnows_test
Data Engineer Test

# Description :
Tried to find the ways to identify the anomalies in the data ingested / reported. I choose to use python with pandas library as we need to parse csv and randomly pick data out of it. This has better feature to create dataframes out of csv and can apply functions and queries on dataframe. It can be faster compared with SQL on large set of data. We can run my python script with below command .

Linux :
py dataMesurement_anomalies.py

Windows:
python.exe dataMesurement_anomalies.py

# Assumptions while providing the solution for finding problems with the given data:
1.	There shouldn't be any duplicate records with same device UUID and same measurement time or for the same device UUID , there shouldn't be data processed for multiple times.
2.	If the total_bytes processed in the test then it is a successful download.
 
# I captured below anomaly scenarios in my solution:
•	Both successful download  and failure attempts are '1'  
•	Finding duplicate entries (device UUID processed at the same time)
•	Recorded as failed attempt even though all the data is processed(includes 0 byte files)
•	Bytes per second column has negative values
Please note that I have added an extra column when capturing the anomalies in a csv with name 'anomaly_desc'. 


# How can we improve the solution:
1. Analyze the system before making assumptions . Think of maximum possible ways of problematic conditions .
2. Need to implement proper unit tests to  make sure the functionally/approach is correct. 
3. If time allows , we can copy the data in a distributed system and can find the anomalies in a better and fast way possible on very large sets of data.

