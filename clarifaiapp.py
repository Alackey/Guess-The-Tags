from clarifai.client import ClarifaiApi
from random import randint
import imgur


CLARIFAI_APP_ID = "qIhhalvjJu_Rcg6RtAKbi_llpZAjel_e4DYZN1Bn"
CLARIFAI_APP_SECRET = "RkYlk7ZxgelgwIuh8Liqkh-JUwloE_Tr6N2fuDPC"
clarifai_api = ClarifaiApi(CLARIFAI_APP_ID, CLARIFAI_APP_SECRET)  # assumes environment variables are set.


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
