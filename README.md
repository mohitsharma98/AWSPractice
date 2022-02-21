# AWSPractice
Practicing ETL implementation using S3, AWS Glue and Pyspark

### Step 1: Creating S3 Bucket
1. Open S3 console and create bucket
2. Create folder named "input" inside S3 bucket.
3. Create folder named "output" inside S3 bucket to store the transformed data.

### Step 2: Uploading the data inside the S3 Bucket
1. Upload the data present inside /Data folder in this repository into "s3://bucket-name/input" folder created in Step 1

### Step 3: Creating the Glue Crawler
1. Got to AWS Glue Service console page.
2. Click on Crawlers, add crawler button.
3. Give your clrawler a name and click next
4. Specify crawler sorce type as data store and check the crawl all the folders radio button.
5. Select S3 as Data Store and Select input folder as the crawler target from s3 (s3://bucket-name/input)
6. Click on No, to add another data store and click next.
7. Choose create an IAM role (if you don't have one present for existing crawlers), Name is and click next.
8. Select "Run on demand" as a schedule for your crawler and hit next.
9. Click on Add Database option (in case you don't have any databases present to store the schema of the table crawled from s3).
10. Give you database a name and click next.
11. Review your choices and click on finish.

### Step 4: Running your Crawler
1. Go to Crawlers in the AWS Glue Console Page and select the crawler you created in Step 3.
2. Click on Actions and select Run Crawler option.
