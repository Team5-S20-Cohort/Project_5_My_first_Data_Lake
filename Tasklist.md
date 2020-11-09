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
## ToDO:

### **#Harish and Yemi** 
*  We create a IAM user Accounts with appropriate permission. 
### **#Harish and Yemi**
*  A Role to access s3 bucket
### **#Antony and sabe**
*  Create a VPC inside a Region and AZ.
### **#Antony and sabe**
*  Public Subnets and Private subnets 
### **#Antony and sabe**
*  Create appropriate security groups. 
### **#Rogba and sabe**
*  2 EC2 in Public subnets and 1 EC2 in Private Subnet. 
### **Yemi and Harish**
*  Setup MongoDb (Deploy and configuration) in Private subnet. 
### **Antony and Rogba and Yemi and Sabe and Harish**
*  Setup S3 bucket with name: dstiproject5-bucket-n
### **Rogba and Sabe**
*  Upgrade and update the EC2 
### **Yemi and Harish**
*  install docker and make it container 
### **Antony and Rogba(Ahmed)**
*  Add python code into EC2 instanses 
### **Yemi and Harish**
*  Launch Lambda Function 
### **Yemi and Harish**
*  Launch Kafka  by connecting with Lambda function. 
### **Sabe and Harish and Yemi and rogba and Anthony**
*  Write Kafka code to inject and process data 
### **Sabe and Harish and Yemi and rogba and Anthony**
*  write kafka code to clean data.
### **Sabe and Harish and Yemi and rogba and Anthony**
*  process this clean data into MongoDb.
# Prediction: 
**this will be given by Harish and Yemi(Christan). 


