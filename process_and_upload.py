import boto3
import pandas as pd
from datetime import datetime
import os

# -------- CONFIG --------
bucket_name = "us-project01"
input_file = "downloaded_file.bin"   # change if needed

# -------- STEP 1: detect file type --------
file_ext = os.path.splitext(input_file)[1]

if file_ext == ".bin":
    # assume it's csv (common case)
    new_file = "data.csv"
    os.rename(input_file, new_file)
    input_file = new_file

# -------- STEP 2: read file --------
df = pd.read_csv(input_file)

# -------- STEP 3: add partition columns --------
now = datetime.now()
df["year"] = now.strftime("%Y")
df["month"] = now.strftime("%m")

# -------- STEP 4: save processed file --------
processed_file = "processed_data.csv"
df.to_csv(processed_file, index=False)

# -------- STEP 5: upload to S3 --------
s3 = boto3.client("s3")

year = now.strftime("%Y")
month = now.strftime("%m")

s3_key = f"data/year={year}/month={month}/processed_data.csv"

try:
    s3.upload_file(processed_file, bucket_name, s3_key)
    print("Uploaded successfully")
    print("S3 Path:", f"s3://{bucket_name}/{s3_key}")
except Exception as e:
    print("Error:", e)