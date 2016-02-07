from clarifai.client import ClarifaiApi
import imgur
import json
import pprint
clarifai_api = ClarifaiApi()  # assumes environment variables are set.
URLArray = imgur.getImages()
imageURL = URLArray[0]
result = clarifai_api.tag_image_urls(imageURL)
pprint.pprint(result)

