from dotenv import load_dotenv
load_dotenv()

import cloudinary
import cloudinary.api
import cloudinary.uploader

config = cloudinary.config(secure=True)


def get_all_images():
    return cloudinary.Search().execute()
images = get_all_images()

def get_file_names(all_images):
    response = all_images
    return list(map(lambda image: image['filename'], response['resources'][::]))


def interactive_search(query):
    return list(filter(lambda name: name.startswith(query), get_file_names(images)))


def upload_images(title, url):
    cloudinary.uploader.upload(url, 
    public_id = title,
    overwrite = True,
    folder = 'gallery'
    )


def get_images_from_exact_folder(folder_name):
    return cloudinary.Search().expression(f"folder:{folder_name}").execute()


def get_all_folders():
    response = cloudinary.Search().execute()
    not_filtered_folders = list(map(lambda image: image['folder'], response['resources'][::]))
    return list(set(not_filtered_folders))
