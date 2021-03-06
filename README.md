# Project_5_My_first_Data_Lake
## Architecture

* The architecture typically describes the buiding of a datalake for the storage of all forms of data that can be extracted from an open source kaggle repository on the internet. Typically, there are two possible scenarios:
* - Batch Data
* - Streaming Data
 
This project is concerned with ingesting batch data from source by using python scripts and preparing it is such a way that would be easy to extract and display information on a data analytics tool Microsoft PowerBi.

We had to exclude the streaming data because there was no correlation between the weather conditions in France and the Covid-19 data.

The project is a typical ETL procedure


### lastest design
![image](https://user-images.githubusercontent.com/67946241/110204506-aafd5500-7e73-11eb-8499-cfa113ddee68.png)


###About the Data
* The data used for this project is a dataset on Covid-19. It is a dataset that is located at and curled from the url https://www.kaggle.com/hgunraj/covidxct. It is a 29GB data that containes the following files in a zip:
2A_images
metadata.txt
test_COVIDx_CT-2A.txt
train_COVIDx_CT-2A.txt
Val_COVIDx_CT-2A.txt

The Images folder contains images of patients brains who at the time of taking covid tests, either have pneumonia, Covid-19 or normal. For each patient, we have several intrinsic information such as Country, age, sex, disease type (normal, covid or Pneumonia) all linked to the patient ID

### Data Ingestion
* Data ingestion was done by running a python script on an Ubuntu 20.4 ec2 instance in Amazon cloud. To address cost, the ec2 instance used is within the free tier. However, to cater for the relatively huge data size, the storage on the server was increase in excess of required space. There was no requirement to upgrade the ec2 instance as it is a fresh installment from Amazon. 

The EC2 instance was configured as follows:
1. Update the instance by running:
   sudo apt-get update
   ![image](https://user-images.githubusercontent.com/67946241/110030514-25c05600-7d36-11eb-88f9-ef06dcc135c8.png)
   
2. Install pip
   sudo apt install python3-pip
   
   ![image](https://user-images.githubusercontent.com/67946241/110030468-15a87680-7d36-11eb-9f67-bb689cb57bbc.png)
   
3. Create a virtual env named Project5
   python3 -m pip install virtualenv
   Virtualenv Project5
4. Install Boto3 and Kaggle Libraries
   pip install boto3
   pip install kaggle
    

### Data Extraction and Transformation
The python script written does the following:
* Extract the zip files
* Merge the content of the txt file before uploading into the s3 datalake. 
 
The process of extractions and merging required that the data be first uploaded to storage on the ec2 instance, perform the transformation process before uploading the files into s3 bucket. This is because data manipulation in s3 is more complicated.
 
#### Error during extraction
The error below is typical of data extraction from Kaggle:
![image](https://user-images.githubusercontent.com/67946241/110030182-b0ed1c00-7d35-11eb-9db7-d2381c78886f.png)

  ubuntu@ip-172-31-82-159:~/Project5$ python3 project.py
Traceback (most recent call last):
  File "project.py", line 1, in <module>
    from kaggle.api.kaggle_api_extended import KaggleApi
  File "/home/ubuntu/.local/lib/python3.8/site-packages/kaggle/__init__.py", line 23, in <module>
    api.authenticate()
  File "/home/ubuntu/.local/lib/python3.8/site-packages/kaggle/api/kaggle_api_extended.py", line 164, in authenticate
    raise IOError('Could not find {}. Make sure it\'s located in'
OSError: Could not find kaggle.json. Make sure it's located in /home/ubuntu/.kaggle. Or use the environment method.

This error is easily taken care of by downloading the kaggle json file and saving it into the root directory of the ec2 instance /home/ubuntu
The json file is needed to establish connection to kaggle before any data can be extracted.

 ### Data Loading
After unzipping and merging the files, the data is then uploaded to s3 and the update is seen realtime:


### Post-Uploading
During uploading of the files to S3, about 126,000 files were uploaded out of about 196,000 files. This accounts for about 64% success rate. The huge failure experienced was due to the low compute power of the ec2 instance which resulted to throtling during the processing. The free tier ec2 instance runs about 300 iops. To resolve this, the python code was redesigned to go into the folder, make comparison with successful upload and upload the differential:

![image](https://user-images.githubusercontent.com/67946241/110032185-24902880-7d38-11eb-8dc0-99144b68c8d2.png)


This resulted to the uploading of the remaining missing files:

![image](https://user-images.githubusercontent.com/67946241/110032321-4ab5c880-7d38-11eb-856a-211322168ac0.png)


### Data Visualization
 * Now that all the data has been moved to s3, we now have a datalake from which we are set to extract useful information to display on PowerBi. To achieve this, there is a need to install a connector for PowerBI to S3. Establishing a connection between the s3 and PowerBi allows us search for needed information from the datalake and displaying same in powerBi. 
 
 ![image](https://user-images.githubusercontent.com/67946241/110034245-7e91ed80-7d3a-11eb-951f-625ae1973390.png)

