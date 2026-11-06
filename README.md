# SmartCare - AWS Data Engineering Project

**Architecture:** S3 -> Glue ETL -> S3 DW -> Crawler -> Athena -> S3 Dashboard (No QuickSight)

## Tools Used
- AWS S3, Glue, Athena, Crawler
- GitHub, Jenkins, Docker
- Chart.js for Dashboard

## How It Works
1. Raw CSV uploaded to S3 Staging
2. Glue cleans data (nulls, duplicates)
3. Cleaned data saved to S3 DW
4. Crawler creates table
5. Athena runs SQL queries
6. S3 Website shows charts from Athena CSV

## Athena Queries
- Visits by Department
- Patients by Gender
- Total Fees by Department

## Live Dashboard
Hosted on AWS S3 Static Website - No QuickSight Needed