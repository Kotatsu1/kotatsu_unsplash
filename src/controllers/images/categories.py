from fastapi import HTTPException
import cloudinary
import cloudinary.api
from dotenv import load_dotenv
from controllers.images import favorite
from schemas.image_schemas import FetchFromCategory, FetchCategoryFavorites
from utils.favorites import mark_favorite
from utils.page_preview import add_page_preview, text_for_page_preview

load_dotenv()

config = cloudinary.config(secure=True)

def get_categories() -> dict:
    response = cloudinary.api.root_folders()
    for i in response['folders']:
        i['name'] = i['name'].capitalize().replace('-', ' ')
    return response


def get_images_with_params(type: str, cursor: str) -> dict:
    return cloudinary.Search().max_results("50").next_cursor(cursor).expression(f"folder:{type}").execute()


def get_images_from_category(request: FetchFromCategory):
    try:
        images = get_images_with_params(request.folder, request.next_cursor)
        added_preview = add_page_preview(images, request.folder)
        added_text_for_page_preview = text_for_page_preview(added_preview, request.folder)

        return added_text_for_page_preview
    except Exception:
        raise HTTPException(status_code=404, detail='Cound not get images from category')


def get_category_images_with_favorite(request: FetchCategoryFavorites):
    all_images = get_images_with_params(request.category, request.next_cursor)
    added_preview = add_page_preview(all_images, request.category)
    added_text_for_page_preview = text_for_page_preview(added_preview, request.category)
    resources = added_text_for_page_preview['resources']
    favorite_images = favorite.user_favorive_images(request.token)

    updated_resources = list(map(lambda image: mark_favorite(image, favorite_images), resources))
    return {**added_preview, 'resources': updated_resources}
