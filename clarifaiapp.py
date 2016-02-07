from clarifai.client import ClarifaiApi
from random import randint
import imgur

clarifai_api = ClarifaiApi()  # assumes environment variables are set.


def getContent():
    # Get Tags
    URLArray = imgur.getImages()

    result1 = clarifai_api.tag_image_urls(URLArray[0]['url'])
    result2 = clarifai_api.tag_image_urls(URLArray[1]['url'])
    print('for loop')
    tags = []
    count = 0
    for i in range(0, 12):
        rand = randint(0, 1)
        if rand == 0:
            tags.append(result1["results"][0]["result"]["tag"]["classes"][i])
            count += 1
        else:
            tags.append(result2["results"][0]["result"]["tag"]["classes"][i])

    imgDetails = {
        'url': URLArray[0]['url'],
        'tags': result1["results"][0]["result"]["tag"]["classes"],
        'choices': tags,
        'width': URLArray[0]['width'],
        'height': URLArray[0]['height'],
        'numOfTags': count
    }

    return imgDetails
