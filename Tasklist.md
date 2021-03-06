 # Task List :
 ## GITHUB:
  * Create a GITHUB repository for the project
  * Update Readme.md files. 
  * Upload all required files.
  
 ## Create AWS cloud account 
  * Configure Identity and access management.
  * Create users, groups, roles, and policies
  * Create VPC, Gateway security group , private subnets for MongoDB and EC2 instance for storage, and a public subnet for Instances hosting  Tableau
  * Spin up an EC2 instance(Install Updates, apache webserver, and other dependencies for running any scripts to be used here).

* **For Batch Data:**
  * Create a python script that extracts data related to COVID.
  * Get all required data sources that COVID exists. (like website, forums, articles, videos (video stream apps/websites), Analytical sites).


* **Scripts:**
  * Python scripts to clean the data.
  * scritps to load into S3.(Batch data).
  
   
## PowerBI:

 * Install Microsoft PowerBI Server .
 * Establish a connection between s3 bucket and PowerBI.

## Prediction:

 * Finding Time series analysis between COVID data and Weather data.
 * Forecasting effect between COVID and weather in the future.
 
## Todo:

## Improvement Areas:
 * Inclusion of Streaming data if has been available. Collecting data of all API's(On the data sources).
 * The use of Docker for seamless deployments


### **#Anthony and Yemi** 
*  We create a IAM user Accounts with appropriate permission. 
### **#Sabe and Yemi**
*  A Role to access s3 bucket
### **#Antony and Rogba**
*  Create a VPC inside a Region and AZ.
### **#Antony and sabe**
*  Public Subnets and Private subnets 
### **#Antony and Yemi**
*  Create appropriate security groups. 
### **#Rogba and sabe**
*  2 EC2 in Public subnets and 1 EC2 in Private Subnet. 
### **Yemi and Rogba**
*  Setup MongoDb (Deploy and configuration) in Private subnet. 
### **Antony and Rogba and Yemi and Sabe **
*  Setup S3 bucket with name: dstiproject5-bucket-n
### **Rogba and Sabe**
*  Upgrade and update the EC2 
### **Antony and Rogba(Ahmed)**
*  Add python code into EC2 instanses 
### **Yemi and Anthony**
*  Launch Lambda Function 
### **Yemi and Sabe**
*  Launch Kafka  by connecting with Lambda function. 
### **Sabe and Yemi and Yemi and rogba and Anthony**
*  Write Kafka code to inject and process data 
### **Sabe and Rogba and Yemi and rogba and Anthony**
*  write kafka code to clean data.
### **Sabe and Yemi and Yemi and rogba and Anthony**
*  process this clean data into MongoDb.
# Prediction: 
**this will be given by Anthony and Yemi(Christan). 


