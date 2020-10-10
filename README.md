# Project_5_My_first_Data_Lake
## Architecture
* The architecture as shown below features the ingestion of Data into the systems from internet.
* - Batch Data
* - Streaming Data


![Architecture](/datalake.png)

### Data Ingestion
* To commence the process, a python code is used to pull streaming data from available APIs on the web, and send the data to an Apache Kafka instance which is dockerised for easy deployment, management and scalability.
 The same process applys to batch data, which is instead sent to another EC2 instance for storage. An EC2 instance was used to allow us have enough storage for batch data within the free tier available in Amazon cloud.

### Data Cleaning for Batch Data.
* After loading the batch data into storage. A python code is used to clean the data, where only required information are sent to the Mongo DB in readiness for prediction        algorithms and visualization on Tableau.

### Streaming Data processing
* For streaming data, Apache Kafka is used to filter the data and sent to mongo DB. Apache Kafka has the capacity to provide buffer for the incoming data so that the entire       system is not overwhelmed. Mongo DB was used as final storage because of the convinience it provides and capacity to handle different forms of data structure including NOSQL     data which will form part of our data system.  

### Data Visualization
 * Now that the processed data is in mongo DB, prediction analysis will be done and appropriate comparison is carried out between the batch data and the streaming data. The        result is visualized on Tableau.
 
