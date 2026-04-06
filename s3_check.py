# this file check each bucket on s3
# task2 => create new file which will check each bucket on s3 




import boto3
# boto3 see hum aws service like s3 or ec2 service access kar sakte hai

# S3 client
s3 = boto3.client('s3')
# yeh ek s3 client object banata hai iske through hum aws s3 per operations perform karte hai behind the scene yeh aws credentials use karta hai aws configure waale



# List buckets
response = s3.list_buckets()
# iss see aws s3 per ek request jaati hai mere account ke saare buckets baatao response main hume ek dictionary milti hai



print("Your S3 Buckets:\n")
# Sirf output ko clean banane ke liye



for bucket in response['Buckets']:
    #yeh loop har bucket per chalega 
    bucket_name = bucket['Name']
    # har bucket ek dictionary hai usme see hum "Name" key nikal rahe hai
    print(f"Bucket: {bucket_name}")
    # yaha maine f-string yaani ki formatted string use kiya hai formatted string ka matlab => string ke andar hum directly variables use kar sakte hai {bucket_name} => variable ki value isme insert hogi

    

    try:
        # try error ko handle karega agar koi error aa gaya like permission se related, aws credentials se related, network se related etc. toh aapka program crash naa ho try uss error ko handle karega except block main jaake error ko print kar dega
        

        # Check objects inside bucket
        objects = s3.list_objects_v2(Bucket=bucket_name)
        # maine aws ko request bheji hai ki mujhe baatao ki iss bucket ke andar kaun kaun see files present hai yeh bhi ek dictionary return karega jisme "Contents" key hogi agar bucket ke andar files hai toh usme files ki list hogi aur agar bucket khali hai toh "Contents" key nahi hogi



        if 'Contents' in objects:
            # iss line ka matlab hai ki agar "Contents" key objects dictionary main hai toh iska matlab hai ki bucket ke andar files resent hai
            print(f"    {len(objects['Contents'])} files found")
            # yaha per len() number of files ko count karta hai aur usko print karta hai
        else:
            # or agar "Contents" key nahi hai toh iska matlab hai ki bucket khali hai 
            print("    Bucket is empty")

    except Exception as e:
        print(f"    Error: {e}")
        # yaha per agar koi error aati hai toh main uss error ko print kar dunga like network se related error, permission se related error, aws credentials se related error etc. toh yeh line uss error ko print kar degi 
