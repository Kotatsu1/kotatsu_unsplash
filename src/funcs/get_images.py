from dotenv import load_dotenv
load_dotenv()

import cloudinary
import cloudinary.api

config = cloudinary.config(secure=True)



def get_names_from_cloudinary():
    response = cloudinary.Search().execute()
    names_list = []
    for i in range(response['total_count']):
        names_list.append(response['resources'][i]['filename'])
    
    return names_list


def get_all_images():
    return cloudinary.Search().execute()

    
def interactive_search(query):
    return [element for element in get_names_from_cloudinary() if query in element]

