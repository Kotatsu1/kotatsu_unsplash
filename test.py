import requests


CLOUDINARY_NAME="dkdkbllwf"
CLOUDINARY_API_KEY="568255218583821"
CLOUDINARY_API_SECRET="TQmSexgBfsrxFyhwOSL935q5ack"
CLOUDINARY_URL='cloudinary://568255218583821:TQmSexgBfsrxFyhwOSL935q5ack@dkdkbllwf'



def searchPhotos(cdnURL, query):
    response = requests.get(cdnURL)
    storeFilePaths = []
    for fileURL in response.text.split("\n"):
        if query in fileURL:
            storeFilePaths.append(fileURL)
    return storeFilePaths

cdnURL = CLOUDINARY_URL
queryFromCDN = "beach"
photos = searchPhotos(cdnURL, queryFromCDN)
print(photos)