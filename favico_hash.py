# Script that calculates the hash of a favico in order to make further Shodan searches for instance.

import mmh3
import requests
import codecs

response = requests.get(input('Target url: '))
favicon = codecs.encode(response.content, "base64")
hash = mmh3.hash(favicon)
print("Hash of target favicon is:", hash)

