def add_page_preview(data: dict, params: str) -> dict:
    data.update({'page_preview': f'http://45.87.246.48:8000/page_preview/{params}.avif'})
    return data


def text_for_page_preview(data: dict, category: str) -> str:
    categories = {
    "editorial": "The internet's source for visuals.Powered by creators everywhere.",
    "animals": "Exotic wildlife, pet kittens — and everything in between. Uncover the beauty of the animal kingdom through your screen.",
    "anime": "Discover captivating anime pictures featuring diverse characters and stunning animation, ranging from action to romance, drama, and comedy.",
    "architecture-and-interiors": "Exploring our built environments — from brutalist buildings to eccentric home decor. This category showcases the best of architecture and interiors from around the world.",
    "arts-and-culture": "Your daily dose of culture — with photography showcasing the best in art, music and literature from around the world.",
    "fashion-and-beauty": "Fashion and Beauty are a powerful form of self-expression. This category documents style through inspiring shots of street fashion, skincare products, avant-garde editorial photographs, and more.",
    "food-and-drink": "From simple home-cooked dinners at home, to tasting new dishes while traveling — food connects us all. This category examines the world of food photography, with shots of everything from summer picnics in the park to decadent deserts.",
    "greener-cities": "We teamed up with One Tree Planted, and their Urban Forestry Action Fund, to spread the word of the importance of green in our cities on our planet and our health. Submit an image of trees and plants in urban areas — from rooftop forests to trees along sidewalks." ,
    "health-and-wellness": "Celebrate a healthy mind, body and soul with photographs that showcase everything from new medical discoveries and alternative medicines, to healthy eating and meditation.",
    "travel": "Discover hidden wonders and inspiring destinations around the world from the comfort of your own home.",
    "wallpapers": "From epic drone shots to inspiring moments in nature — submit your best desktop and mobile backgrounds.",
    }

    data.update({'text_for_page_preview': f'{categories[category]}'})
    return data