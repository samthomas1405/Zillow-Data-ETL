# Zillow Data ETL Pipeline
This repository contains code for an end-to-end ETL pipeline with Apache Airflow using Python bash scripts in order to migrate data to the AWS cloud. Uses Zillow RapidAPI to extract real estate property data of 123 properties from Fishkill, New York, transform the data into a csv file using Amazon lambda functions, and then load the clean data into an Amazon s3 bucket. The pipeline then transfers clean data into an Amazon Redshift cluster to perform analytics and connects the cluster to Amazon QuickSight to visualize various data models.

## Pipeline Architecture
<img width="1299" alt="architecture" src="https://github.com/user-attachments/assets/2d9e73ba-36fd-425e-8df5-c408373b8205">

## DAG View
<img width="904" alt="dag" src="https://github.com/user-attachments/assets/c4fe401c-8810-41bb-8438-e878ad1519e6">

## QuickSight Analytics
<img width="808" alt="zillow_analytics" src="https://github.com/user-attachments/assets/0e5be674-5d6e-4cfa-910b-bf6d920599d2">


