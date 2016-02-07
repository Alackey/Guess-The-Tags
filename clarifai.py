from clarifai.client import ClarifaiApi
import imgur
import json
import pprint
clarifai_api = ClarifaiApi()  # assumes environment variables are set.
URLArray = imgur.getImages()
imageURL = URLArray[0]
result = clarifai_api.tag_image_urls(imageURL)



def writeToFile(result):
    with open('data.txt', 'w') as outfile:
        json.dump(result, outfile)
    outfile.close()
    
def getTags(result):
    
    tags = result["results"][0]["result"]["tag"]["classes"]
    
    return tags
#pprint.pprint(result)
#pprint.pprint(result["results"][0]["result"]["tag"]["classes"])
#getTags(result)

