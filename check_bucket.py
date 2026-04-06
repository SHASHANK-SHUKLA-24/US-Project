import boto3

def check_bucket_exists(bucket_name):
    # yaha maine function create kiya hai jiska naam hai check_bucket_exists aur yeh function ek argument lega jiska naam hai bucket_name jisme hum bucket ka naam pass karenge jisko hum check karna chahte hai ki wo bucket exist karta hai ya nahi
    s3 = boto3.client('s3')
    # aws s3 see connect karne ke liye maine boto3 client create kiya hai jiska naam s3 hai iske through hum aws s3 per operations perform karte hai behind the scene yeh aws credentials use karta hai aws configure waale

    # saare buckets fetch karo
    response = s3.list_buckets()
    # yeh command mujhe mere account ke saare buckets ke baare mein baatyegi
    # yaha per maine aws s3 ko request bheji hai ki mujhe mere account ke saare buckets ke baare mein batao yeh bhi ek dictionary return karega jisme "Buckets" key hogi aur usme buckets ki list hogi


    # bucket names extract karo
    bucket_list = [bucket['Name'] for bucket in response['Buckets']]
# yeh list comprehension hai jisme hum response dictionary ke "Buckets" key se har bucket ke "Name" key ko extract kar rahe hai aur usko ek list main store kar rahe hai jiska naam bucket_list hai




    # check karo input bucket list mein hai ya nahi
    if bucket_name in bucket_list:
        # yeh check karta hai ki jo bucket_name humne function ko pass kiya hai wo bucket_list mein hai ya nahi agar hai toh iska matlab hai ki bucket exist karta hai aur agar nahi hai toh iska matlab hai ki bucket exist nahi karta hai
        print(f" Bucket '{bucket_name}' exists")
        # agar bucket exist karta hai toh main yeh print kar dunga ki bucket exist karta hai
    else:
        print(f" Bucket '{bucket_name}' does NOT exist")
        # agar bucket exist nahi karta hai toh main yeh print kar dunga ki bucket exist nahi karta hai


# call the function and pass the bucket name
check_bucket_exists("us-project01")