from kaggle.api.kaggle_api_extended import KaggleApi
import os
import sys
import boto3
import glob

#directory
local_directory = "./dataset/"  
bucket = 'dstiproject5-bucket1'
destination = 'covid_dataset'

ACCESS_KEY = 'AKIAIOA6LH6FC6W2TB7Q'
SECRET_KEY = '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'


client = boto3.client('s3', aws_access_key_id=ACCESS_KEY,
                      aws_secret_access_key=SECRET_KEY)



def download_kaggle(kaggle_dataset):
    api = KaggleApi()
    api.authenticate()
    api.dataset_download_files(kaggle_dataset, path = "./dataset/", unzip=True)



def merge_clean_files():
    filenames = glob.glob('./dataset/*.txt')
    with open('./dataset/COVIDx_CT-2A.txt', 'w') as outfile:
        for fname in filenames:
            with open(fname) as infile:
                for line in infile:
                    outfile.write(line)


def upload_to_S3():
    # enumerate local files recursively
    for root, dirs, files in os.walk(local_directory):
        for filename in files:
            local_path = os.path.join(root, filename)
            relative_path = os.path.relpath(local_path, local_directory)
            s3_path = os.path.join(destination, relative_path)
            try:
                client.head_object(Bucket=bucket, Key=s3_path)
            except:
                print("Uploading {}...".format(s3_path))
                client.upload_file(local_path, bucket, s3_path)
                

if __name__ == '__main__':
    print("Downloading dataset from kaggle >>>>>>>>>>>>>>>> \n")
    download_kaggle('imdevskp/corona-virus-report')
    print("Kaggle dataset successfully downloaded and commencing file merging and cleansing >>>>>>>>>>> \n")
    merge_clean_files()
    print("file merged successfully; uploading to S3 \n")
    upload_to_S3()
    print("uploading to S3 successful. \n")
    print("Thank you")