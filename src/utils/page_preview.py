def add_page_preview(data: dict, params: str) -> dict:
    data.update({'page_preview': f'http://45.87.246.48:8000/page_preview/{params}.avif'})
    return data