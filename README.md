# Using AWS Glue, S3, and PySpark to implement ETL in AWS
Practicing ETL implementation using S3, AWS Glue, and Pyspark

### Step 1: Creating S3 Bucket
1. Open the S3 console and create a bucket
2. Create a folder named "input" inside the S3 bucket.
3. Create a folder named "output" inside the S3 bucket to store the transformed data.

### Step 2: Uploading the data inside the S3 Bucket
1. Upload the data present inside /Data folder in this repository into the "s3://bucket-name/input" folder created in Step 1

### Step 3: Creating the Glue Crawler
1. Got to AWS Glue Service console page.
2. Click on Crawlers, add crawler button.
3. Give your crawler a name and click next
4. Specify crawler source type as datastore and check the crawl all the folders radio button.
5. Select S3 as Data Store and Select input folder as the crawler target from s3 (s3://bucket-name/input)
6. Click on No, to add another datastore and click next.
7. Choose to create an IAM role (if you don't have one present for existing crawlers), Name it, and click next.
8. Select "Run on demand" as a schedule for your crawler and hit next.
9. Click on Add Database option (in case you don't have any databases present to store the schema of the table crawled from s3).
10. Give your database a name and click next.
11. Review your choices and click on finish.

### Step 4: Running Glue Crawler
1. Go to Crawlers in the AWS Glue Console Page and select the crawler you created in Step 3.
2. Click on Actions and select the Run Crawler option.

### Step 5: Creating Glue Job
1. Once your crawler is run successfully, you will be able to see the table metadata schema under (Databases > Tables > input)
2. Now click on Glue job and add job option
3. Configure Job properties like name, IAM role, and under Job Parameters change the worker node to 2, click next.
4. Choose the existing data catalog that we crawled in Step 4 as a data source, click next.
5. Choose Transformation as Change Schema (which we will overwrite with our use case.)
6. Choose data target as same input data catalog table we crawled, click next.
7. Click on save the job and Edit the script.

### Step 6: Overwriting the auto-generated script
1. Copy and paste the contents of the /PySpark Scripts/GlueScript.py file to the script shown on the screen.
2. This script is applying a simple transformation just for learning and testing purposes, you can write more complex transformations according to your use case.
3. If you get lost on the page just follow => (select the glue job > actions > edit script)
4. Click on the save button to save your change in the script.
5. Click on Run Job.

## Step 7: Validation and Troubleshooting
1. Once your Job is run successfully, you will be able to see the partition stored inside your output folder inside your s3 bucket created in Step 1.
2. If your job is stuck at some error, please check failure logs (AWS Glue console > select the job > History > ErrorLogs) in AWS CloudWatch.
