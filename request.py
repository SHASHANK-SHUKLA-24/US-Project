# task1 => divide data in chunks

import requests
# requests ek Python library hai
# Iska use HTTP request bhejne ke liye hota hai (GET, POST etc.)

url = "https://transtats.bts.gov/PREZIP/"  # working test file
# yaha maine ek 100 mb ki file donload ki hai for testing

response = requests.get(url, stream=True, verify=False)
# requests.get(url) main server ko get request bhej raha hu
# stream = true ka matlab file chunks part main aayegi puri file ek baar mai nahi aayegi agar stream = true nahi hota puri file ram main load ho jaati


# verify = False ka matlab yeh SSL certificate check skip kar raha hai
# yeh Sirf testing ke liye use hota hai


if response.status_code == 200:
    with open("downloaded_file.bin", "wb") as f:
# "wb" = write binary mode kyunki file binary format main ho sakti hai like images, videos, zip etc.
# with use karne ka fayda:
# File automatically close ho jaati hai
        for chunk in response.iter_content(chunk_size=1024):
            if chunk:
                f.write(chunk)

                # iter_content():=> data ko chote chote parts main divide karta hai

                # chunk_size=1024 ka matlab hai ki 1 KB ke parts main data aayega

    print("Download completed")
else:
    print("Download failed")

# yaha 200 ka matlab hai ki request successful thi file mil gayi 
# 404 ka matlab file nahi mili
# 500 ka matlab server error


# f.write see main har ek chunk ko file main add kar raha hu

# if chunk: => kya kar raha hai ki kabhi kabhi empty chunk aa sakte hai isliye maine yeh check lagaye hai


