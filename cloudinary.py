import cloudinary

import json


CLOUDINARY_URL='cloudinary://568255218583821:TQmSexgBfsrxFyhwOSL935q5ack@dkdkbllwf'


cloudinary.config( 
  cloud_name = "dkdkbllwf", 
  api_key = "568255218583821", 
  api_secret = "TQmSexgBfsrxFyhwOSL935q5ack",
  secure = True
)


image_info=cloudinary.api.resource("beach")
print("****3. Get and use details of the image****\nUpload response:\n", json.dumps(image_info,indent=2), "\n")

