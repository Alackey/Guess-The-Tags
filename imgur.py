from imgurpython import ImgurClient

client_id = '7cacbecc444c8b3'
client_secret = '109435feb9c906d1b73ff4835951e11d012e4b7b'

client = ImgurClient(client_id, client_secret)

# Example request
items = client.gallery()
for item in items:
    print(item.link)
