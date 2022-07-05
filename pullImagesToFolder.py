import requests, os, json, re, time
from tqdm import tqdm
home = os.getcwd()
cardData = 'cardData.json'
IdFile = 'cardID.json'
baseImages = home + '/baseImages/'
imgUrl = 'https://storage.googleapis.com/ygoprodeck.com/pics/'


def cDict():
    cardId = []
    cardName = []

    with open(os.path.join(home, cardData), 'rb') as a:
        data = json.load(a)
        a.close()

    for card in data['data']:
        cardId.append(card['id'])
        cardName.append(card['name'])

    cardName = [re.sub('[:☆★/"!?]', '', item) for item in cardName]
    cardName = [re.sub('[-]', ' ', item) for item in cardName]
    cardName = [re.sub('\s\s+', ' ', item) for item in cardName]
    cardName = [re.sub(r'\s+$', '', item) for item in cardName]

    cD = {cardId[i]: cardName[i] for i in range(len(cardId))}

    return cD


def idMaker(d, name):
    ids = [k for k, v in d.items() if v == name]
    if ids:
        return ids[0]
    return None


if not os.path.isdir(baseImages):
    os.mkdir(baseImages)
    print('Created base image folder\n')
else:
    print('Base image folder exists\n')


cardDict = cDict()

print("Please wait while images are downloaded\n")

for ids, names in tqdm(cardDict.items()):

    if not os.path.isdir(os.path.join(baseImages, str(cardDict.get(ids)))):
        os.makedirs(os.path.join(baseImages, str(cardDict.get(ids))))
        print('Created the image folder')

    direc = (baseImages + str(cardDict.get(ids)) + '/')
    os.chdir(direc)
    print(direc)

    if os.path.exists(direc + names + '.jpg'):
        print('Picture exists\n')
        continue

    with open(names+'.jpg', 'wb') as f:
        fetch = requests.get(imgUrl + str(idMaker(cardDict, names)) + '.jpg')
        f.write(fetch.content)
        f.close()
        time.sleep(0.08)
    os.chdir(baseImages)
