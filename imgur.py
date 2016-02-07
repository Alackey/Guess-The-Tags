from imgurpython import ImgurClient
from random import randint

client_id = '7cacbecc444c8b3'
client_secret = '109435feb9c906d1b73ff4835951e11d012e4b7b'

client = ImgurClient(client_id, client_secret)


def randomSection():
    randInt = randint(1, 3)
    if randInt == 1:
        return 'hot'
    elif randInt == 2:
        return 'top'
    else:
        return 'user'


def randomSort():
    randInt = randint(1, 4)
    if randInt == 1:
        return 'viral'
    elif randInt == 2:
        return 'top'
    elif randInt == 3:
        return 'time'
    else:
        return 'rising'


def randomPage():
    return randint(1, 10)


def randomWindow():
    randWindow = randint(1, 5)
    if randomWindow == 1:
        return 'day'
    elif randomWindow == 2:
        return 'week'
    elif randomWindow == 3:
        return 'month'
    elif randomWindow == 4:
        return 'year'
    else:
        return 'all'


def isJPG(img):
    strJPG = ""
    try:
        strJPG = img.link.split('/')[3].split('.')[1]
    except:
        pass
    if strJPG == 'jpg':
        return True
    return False


def getSearchImages(query):
    items = client.gallery_search(
        query,
        advanced=None,
        sort=randomSort,
        window=randomWindow,
        page=randomPage
    )

    images = []
    for img in items:
        if isJPG(img):
            images.append(img.link)
    return images


def getImages():
    items = client.gallery_search(
        'animal',
        advanced=None,
        sort=randomSort,
        window=randomWindow,
        page=randomPage
    )
    images = []
    for img in items:
        if isJPG(img):
            images.append(img.link)
    return images

items = getImages()
#for item in items:
    #print(item)
