 # Task List :
 ## GITHUB:
  * Create a GITHUB repository for the project
  * Update Readme.md files. 
  * uploade all required files.
  
 ## Create AWS cloud account 
  * Configure Identity and access management.
  * Create users, groups, roles, and policies
  * Create VPC, Gateway security group , private subnets for MongoDB and EC2 instance for storage, and a public subnet for Instances hosting  Tableau
  * Spin up an EC2 instance(Install Updates, apache webserver, and other dependencies for running any scripts to be used here).

* **For Batch Data:**
  * Create a python script that extracts data related to COVID.
  * Get all required data sources that COVID exists. (like website, forums, articles, videos (video stream apps/websites), Analytical sites).
* **For Stream Data:**
  * Collecting data of all API's(On the data sources).

* **Scripts:**
  * Python scripts to clean the data.
  * scritps to load into MongoDB.(Batch data).
  * Scripts to load into MongoDB.(Stream Data).
  
* **MongoDB:**
  * Installing and configuring MongoDB.
 
## On EC2 instance install Docker:

 * Create/Build a docker container.
 * Create folders for File storage
 * Create a Python Scripts to extract batch Data from the web and move to storage.
 * Create a python Scripts to extract Stream data and move to Kafka.
 * Unit Tests the scripts


## Tableau:

 * Install Tableau Server in Docker container.
 * Establish a connection between MongoDB and Tableau.

## Prediction:

 * Finding Time series analysis between COVID data and Weather data.

 * Forecasting effect between COVID and weather in the future.
