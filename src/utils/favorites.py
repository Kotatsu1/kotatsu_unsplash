def mark_favorite(image, favorite_images):
    public_id = image['public_id']
    if public_id in favorite_images:
        return {**image, 'favorite': True}
    else:
        return {**image, 'favorite': False}