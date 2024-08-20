# Zillow Data ETL Pipeline
This repository contains code for an end-to-end ETL pipeline with Apache Airflow using Python bash scripts in order to migrate data to the AWS cloud. Uses Zillow RapidAPI to extract real estate property data of 123 properties from Fishkill, New York, transform the data into a csv file using Amazon lambda functions, and then load the clean data into an Amazon s3 bucket. The pipeline then transfers clean data into an Amazon Redshift cluster to perform analytics and connects the cluster to Amazon QuickSight to visualize various data models.

## Pipeline Architecture
<img width="1322" alt="architecture" src="https://github.com/user-attachments/assets/b17b7d3c-5215-4380-a963-fe7583872710"><br><br>
Displayed above is a diagram that models the flow of the data pipeline. Here is a detailed explanation of the 9 pipeline steps:<br><br>

1. Zillow API: The Zillow RapidAPI is used to fetch data of 123 properties from Fishkill, New York.
2. Python: Python script is utilized to extract data from the API in JSON format.
3. 1st S3 Bucket: Extracted data is transferred into an AWS S3 bucket for further processing.
4. 1st Lambda Function: A lambda function is triggered to copy the raw JSON data to ensure the original data is preserved.
5. 2nd S3 Bucket: The copied data is transferred into a second S3 bucket.
6. 2nd Lambda Function: A second lambda function is triggered to transform the JSON data into a csv file with selective categories such as number of bathrooms, number of bedrooms, price, total area, etc.
7. 3rd S3 Bucket. The transformed data is then transferred into a third S3 bucket.
8. Amazon Redshift: The csv data is transferred into an Amazon Redshift cluster for accessible data storage and analysis.
9. Amazon QuickSight: The Amazon Redshift cluster is imported into Amazon QuickSight in order to provide elaborate visualizations of the data from the 123 properties.

## DAG View
<img width="904" alt="dag" src="https://github.com/user-attachments/assets/c4fe401c-8810-41bb-8438-e878ad1519e6">

## QuickSight Analytics
<img width="808" alt="zillow_analytics" src="https://github.com/user-attachments/assets/0e5be674-5d6e-4cfa-910b-bf6d920599d2">


