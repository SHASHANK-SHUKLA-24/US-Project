# task4 => create new file and create function which will take a name as a parameter and will check agar bucket s3 per nahi hai toh aapke liye bucket banayega or bucket present hai toh print karega bucket already present



import boto3
# boto3 see hum aws service like s3 ya ec2 service access kar sakte hai

from botocore.exceptions import ClientError
# jab hum aws per request bhejte hai aur aws usko process nahi kar paata hai tab yeh clienterror aata hai (aws api call fail hone per error throw hota hai)

def create_bucket_if_not_exists(bucket_name):
    # yeha maine function create kiya hai jiska naam hai create_bucket_if_not_exists aur yeh function ek argument lega jiska naam hai bucket_name jisme hum bucket ka naam pass karenge jisko hum check karna chahte hai ki wo bucket exist karta hai ya nahi agar exist nahi karta hai toh usko create karna hai
    s3 = boto3.client('s3')
    # aws s3 see connect karne ke liye maine boto3 client create kiya hai jiska naam s3 hai iske through hum aws s3 per operations perform karte hai behind the scene yeh aws credentials use karta hai aws configure waale 


    try:
        # try error ko handle karega agar koi error aa gaya like permission se related, aws credentials se related, network se related etc. toh aapka program crash naa ho try uss error ko handle karega except block main jaake error ko print kar dega
        # check if bucket exists
        s3.head_bucket(Bucket=bucket_name)
        # head_bucket command se hum check karte hai ki bucket exist karta hai ya nahi agar bucket exist karta hai toh yeh command successfully execute ho jayega aur agar bucket exist nahi karta hai toh yeh command fail ho jayega aur clienterror throw karega jisko hum except block main handle karenge(yaha maine ek lightweight api call ki hai)
        print(f" Bucket '{bucket_name}' already exists")
        # agar bucket exist karta hai toh main yeh print kar dunga ki bucket already exist karta hai

    except ClientError as e:
        error_code = int(e.response['Error']['Code'])
        # agar bucket exist nahi karta hai toh head_bucket command fail ho jayega aur clienterror throw karega jisko hum except block main handle karenge yaha per maine error code ko extract kiya hai jisse hum check kar sakte hai ki error ka type kya hai agar error code 404 hai toh iska matlab hai ki bucket exist nahi karta hai aur agar error code 403 hai toh iska matlab hai ki permission se related error hai etc. toh yeh line uss error code ko extract kar degi(agar meri aws api call fail hui toh main yeh code run karunga aur isme jo "e" hai iss "e" ke andar saari error information hoti hai)
        # yaha code ka matlab hai error ka type kya hai jaise ki 404, 403, 500 etc.  
        # int() function se error code ko integer main convert kar diya hai kyunki aws api call fail hone par error code string format main aata hai aur hum usko integer format main compare karna chahte hai toh maine int() function use kiya hai

        # agar bucket exist nahi karta
        if error_code == 404:
            # yeh mujhe aws api call fail hone par error code dega agar error code 404 hai toh iska matlab hai ki bucket exist nahi karta hai
            print(f" Bucket '{bucket_name}' not found, creating now...")


            # bucket create karo
            s3.create_bucket(
                Bucket=bucket_name,
                CreateBucketConfiguration={
                    'LocationConstraint': 'ap-south-1'
                }
            )
            # yaha per maine aws s3 ko request bheji hai ki mujhe ek bucket create karna hai jiska naam bucket_name hai aur uska location constraint ap-south-1 hai yeh command successfully execute ho jayega
            print(f" Bucket '{bucket_name}' created successfully")

        else:
            # agar permission se related error hai ya koi aur error hai toh usko print kar do
            print(f" Error: {e}")


# function calling
create_bucket_if_not_exists("us-project01")
# create_bucket_if_not_exists("shashank-24")
