# Project_5_My_first_Data_Lake
## Architecture

* The architecture typically describes the buiding of a datalake for the storage of all forms of data that can be extracted from an open source kaggle repository on the internet. Typically, there are two possible scenarios:
* - Batch Data
* - Streaming Data
 This project is concerned with ingesting batch data from source by using python scripts and preparing it is such a way that would be easy to extract and display information on a data analytics tool such as Tableau or Microsoft PowerBi.

The project is a typical ETL procedure


### lastest design ![Architecture](/pylab.jpg)
![Architecture](/datalake.png)

###About the Data
* The data used for this project is a dataset on Covid-19. It is a dataset that is located at and curled from the url https://www.kaggle.com/hgunraj/covidxct. It is a 29GB data that containes the following files in a zip:
2A_images
metadata.txt
test_COVIDx_CT-2A.txt
train_COVIDx_CT-2A.txt
Val_COVIDx_CT-2A.txt

The Images folder contains images of patients brains who at the time of taking covid tests, either have pneumonia, Covid-19 or normal.

### Data Ingestion
* Data ingestion was done by running a python script on an Ubuntu 20.4 ec2 instance in Amazon cloud. To address cost, the ec2 instance used is within the free tier. However, to cater for the relatively huge data size, the storage on the server was increase in excess of required space. There was no requirement to upgrade the ec2 instance as it is a fresh installment from Amazon. 

The EC2 instance was configured as follows:
1. Update the instance by running:
   sudo apt-get update
2. Install pip
   sudo apt install python3-pip
3. Create a virtual env named Project5
   python3 -m pip install virtualenv
   Virtualenv Project5
4. Install Boto3 and Kaggle Libraries
   pip install boto3
   pip install kaggle
    

### Data Extraction, Transformation and Loading
The python script written does the following:
* Extract the zip files
* Merge the content of the txt file before uploading into the s3 datalake. 
 
The process of extractions and merging required that the data be first uploaded to storage on the ec2 instance, perform the transformation process before uploading the files into s3 bucket. This is because data manipulation in s3 is more complicated.
 
#### Error during extraction
The error below is typical of data extraction from Kaggle:
     

### Data Visualization
 * Now that the processed data is in mongo DB, prediction analysis will be done and appropriate comparison is carried out between the batch data and the streaming data. The        result is visualized on Tableau.
 
