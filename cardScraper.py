import json, requests, os
home = os.getcwd()


def getCardData():
    cardInfo = 'https://db.ygoprodeck.com/api/v7/cardinfo.php'
    r = requests.get(cardInfo)
    cardData = r.content
    cards = 'cardData.json'

    if os.path.isfile(os.path.join(home, cards)) is True:
        print("Card Data Exists")

    if os.path.isfile(os.path.join(home, cards)) is False:
        with open(cards, 'wb') as a:
            a.write(cardData)
            a.close()

        with open(cards, 'r') as b:
            prettyD = json.load(b)

        with open(cards, 'w') as fileName:
            json.dump(prettyD, fileName, indent=3)
            b.close()


def pullIds():
    cards = 'cardData.json'
    cardID = 'cardID.json'
    iden = []

    if os.path.isfile(os.path.join(home, cardID)) is True:
        print("Card Ids Exist")
    if os.path.isfile(os.path.join(home,cardID)) is False:
        with open(os.path.join(home, cards),'r') as c:
            data = json.load(c)
            c.close()
        for card in data['data']:
            iden.append(str(card['id']))
        with open(os.path.join(home, cardID), 'w') as d:
            d.write('\n'.join(iden))
            d.close()


getCardData()
pullIds()
