import random

product_data = []
product_list = [
    "https://us.shein.com/ROMWE-Guys-Letter-Butterfly-Graphic-Tee-p-11615853-cat-1980.html?src_identifier=on%3DBanner%60cn%3DCategory%60hz%3DTops%60ps%3D5_1%60jc%3Dreal_1970&src_module=MenHomePage&src_tab_page_id=page_home1667595968031&mallCode=1&scici=MenHomePage~~ON_Banner,CN_Category,HZ_Tops,HI_hotZoneljx1lbuudja~~5_1~~real_1970~~~~"
    "https://us.shein.com/ROMWE-Guys-Butterfly-Print-Tee-p-11308987-cat-1980.html?src_identifier=on%3DBanner%60cn%3DCategory%60hz%3DTops%60ps%3D5_1%60jc%3Dreal_1970&src_module=MenHomePage&src_tab_page_id=page_home1667595968031&mallCode=1&scici=MenHomePage~~ON_Banner,CN_Category,HZ_Tops,HI_hotZoneljx1lbuudja~~5_1~~real_1970~~~~",
    "https://us.shein.com/SHEIN-Men-Cartoon-Letter-Graphic-Tee-p-10969983-cat-1980.html?src_identifier=on%3DBanner%60cn%3DCategory%60hz%3DTops%60ps%3D5_1%60jc%3Dreal_1970&src_module=MenHomePage&src_tab_page_id=page_home1667595968031&mallCode=1&scici=MenHomePage~~ON_Banner,CN_Category,HZ_Tops,HI_hotZoneljx1lbuudja~~5_1~~real_1970~~~~",
    "https://us.shein.com/ROMWE-Guys-Letter-Butterfly-Graphic-Tee-p-11459639-cat-1980.html?src_identifier=fc%3DMen%60sc%3DTOPS%60tc%3D0%60oc%3D0%60ps%3Dtab05navbar05%60jc%3Dreal_1970&src_module=topcat&src_tab_page_id=page_real_class1667596124610&mallCode=1&scici=navbar_MenHomePage~~tab05navbar05~~5~~real_1970~~~~0",
    "https://us.shein.com/SHEIN-Men-Drawstring-Waist-Paisley-Print-Shorts-p-2589248-cat-1976.html?src_identifier=fc%3DMen%60sc%3DBOTTOMS%60tc%3D0%60oc%3D0%60ps%3Dtab05navbar06%60jc%3Dreal_2045&src_module=topcat&src_tab_page_id=page_goods_detail1667596130841&mallCode=1&scici=navbar_MenHomePage~~tab05navbar06~~6~~real_2045~~~~0",
    "https://us.shein.com/Men-Letter-Graphic-Striped-Trim-Drawstring-Waist-Shorts-p-10633322-cat-1976.html?src_identifier=fc%3DMen%60sc%3DBOTTOMS%60tc%3D0%60oc%3D0%60ps%3Dtab05navbar06%60jc%3Dreal_2045&src_module=topcat&src_tab_page_id=page_goods_detail1667596130841&mallCode=1&scici=navbar_MenHomePage~~tab05navbar06~~6~~real_2045~~~~0",
    "https://us.shein.com/Men-Drawstring-Waist-Cargo-Pants-p-11134833-cat-1978.html?src_identifier=fc%3DMen%60sc%3DBOTTOMS%60tc%3D0%60oc%3D0%60ps%3Dtab05navbar06%60jc%3Dreal_2045&src_module=topcat&src_tab_page_id=page_goods_detail1667596130841&mallCode=1&scici=navbar_MenHomePage~~tab05navbar06~~6~~real_2045~~~~0",
    "https://us.shein.com/ROMWE-Guys-Letter-Wings-Graphic-Drawstring-Sweatpants-p-11698533-cat-2988.html?src_identifier=fc%3DMen%60sc%3DBOTTOMS%60tc%3D0%60oc%3D0%60ps%3Dtab05navbar06%60jc%3Dreal_2045&src_module=topcat&src_tab_page_id=page_goods_detail1667596130841&mallCode=1&scici=navbar_MenHomePage~~tab05navbar06~~6~~real_2045~~~~0"
    "https://us.shein.com/ROMWE-Guys-Lightning-Graphic-Drawstring-Shorts-p-2798518-cat-1976.html?src_identifier=fc%3DMen%60sc%3DBOTTOMS%60tc%3D0%60oc%3D0%60ps%3Dtab05navbar06%60jc%3Dreal_2045&src_module=topcat&src_tab_page_id=page_goods_detail1667596130841&mallCode=1&scici=navbar_MenHomePage~~tab05navbar06~~6~~real_2045~~~~0"
]

# Initialize jokes
def initJokes():
    # setup jokes into a dictionary with id, joke, haha, boohoo
    item_id = 0
    for item in product_list:
        product_data.append({"id": item_id, "joke": item, "haha": 0, "boohoo": 0})
        item_id += 1
    # prime some haha responses
    for i in range(10):
        id = getRandomJoke()['id']
        addJokeHaHa(id)
    # prime some haha responses
    for i in range(5):
        id = getRandomJoke()['id']
        addJokeBooHoo(id)
        
# Return all jokes from product_data
def getJokes():
    return(product_data)

# Joke getter
def getJoke(id):
    return(product_data[id])

# Return random joke from product_data
def getRandomJoke():
    return(random.choice(product_data))

# Liked joke
def favoriteJoke():
    best = 0
    bestID = -1
    for joke in getJokes():
        if joke['haha'] > best:
            best = joke['haha']
            bestID = joke['id']
    return product_data[bestID]
    
# Jeered joke
def jeeredJoke():
    worst = 0
    worstID = -1
    for joke in getJokes():
        if joke['boohoo'] > worst:
            worst = joke['boohoo']
            worstID = joke['id']
    return product_data[worstID]

# Add to haha for requested id
def addJokeHaHa(id):
    product_data[id]['haha'] = product_data[id]['haha'] + 1
    return product_data[id]['haha']

# Add to boohoo for requested id
def addJokeBooHoo(id):
    product_data[id]['boohoo'] = product_data[id]['boohoo'] + 1
    return product_data[id]['boohoo']

# Pretty Print joke
def printJoke(joke):
    print(joke['id'], joke['joke'], "\n", "haha:", joke['haha'], "\n", "boohoo:", joke['boohoo'], "\n")

# Number of jokes
def countJokes():
    return len(product_data)

# Test Joke Model
if __name__ == "__main__": 
    initJokes()  # initialize jokes
    
    # Most likes and most jeered
    best = favoriteJoke()
    print("Most liked", best['haha'])
    printJoke(best)
    worst = jeeredJoke()
    print("Most jeered", worst['boohoo'])
    printJoke(worst)
    
    # Random joke
    print("Random joke")
    printJoke(getRandomJoke())
    
    # Count of Jokes
    print("Jokes Count: " + str(countJokes()))

    import random

products_data = []
product_list = [
    "https://us.shein.com/ROMWE-Guys-Letter-Butterfly-Graphic-Tee-p-11615853-cat-1980.html?src_identifier=on%3DBanner%60cn%3DCategory%60hz%3DTops%60ps%3D5_1%60jc%3Dreal_1970&src_module=MenHomePage&src_tab_page_id=page_home1667595968031&mallCode=1&scici=MenHomePage~~ON_Banner,CN_Category,HZ_Tops,HI_hotZoneljx1lbuudja~~5_1~~real_1970~~~~"
    "https://us.shein.com/ROMWE-Guys-Butterfly-Print-Tee-p-11308987-cat-1980.html?src_identifier=on%3DBanner%60cn%3DCategory%60hz%3DTops%60ps%3D5_1%60jc%3Dreal_1970&src_module=MenHomePage&src_tab_page_id=page_home1667595968031&mallCode=1&scici=MenHomePage~~ON_Banner,CN_Category,HZ_Tops,HI_hotZoneljx1lbuudja~~5_1~~real_1970~~~~",
    "https://us.shein.com/SHEIN-Men-Cartoon-Letter-Graphic-Tee-p-10969983-cat-1980.html?src_identifier=on%3DBanner%60cn%3DCategory%60hz%3DTops%60ps%3D5_1%60jc%3Dreal_1970&src_module=MenHomePage&src_tab_page_id=page_home1667595968031&mallCode=1&scici=MenHomePage~~ON_Banner,CN_Category,HZ_Tops,HI_hotZoneljx1lbuudja~~5_1~~real_1970~~~~",
    "https://us.shein.com/ROMWE-Guys-Letter-Butterfly-Graphic-Tee-p-11459639-cat-1980.html?src_identifier=fc%3DMen%60sc%3DTOPS%60tc%3D0%60oc%3D0%60ps%3Dtab05navbar05%60jc%3Dreal_1970&src_module=topcat&src_tab_page_id=page_real_class1667596124610&mallCode=1&scici=navbar_MenHomePage~~tab05navbar05~~5~~real_1970~~~~0",
    "https://us.shein.com/SHEIN-Men-Drawstring-Waist-Paisley-Print-Shorts-p-2589248-cat-1976.html?src_identifier=fc%3DMen%60sc%3DBOTTOMS%60tc%3D0%60oc%3D0%60ps%3Dtab05navbar06%60jc%3Dreal_2045&src_module=topcat&src_tab_page_id=page_goods_detail1667596130841&mallCode=1&scici=navbar_MenHomePage~~tab05navbar06~~6~~real_2045~~~~0",
    "https://us.shein.com/Men-Letter-Graphic-Striped-Trim-Drawstring-Waist-Shorts-p-10633322-cat-1976.html?src_identifier=fc%3DMen%60sc%3DBOTTOMS%60tc%3D0%60oc%3D0%60ps%3Dtab05navbar06%60jc%3Dreal_2045&src_module=topcat&src_tab_page_id=page_goods_detail1667596130841&mallCode=1&scici=navbar_MenHomePage~~tab05navbar06~~6~~real_2045~~~~0",
    "https://us.shein.com/Men-Drawstring-Waist-Cargo-Pants-p-11134833-cat-1978.html?src_identifier=fc%3DMen%60sc%3DBOTTOMS%60tc%3D0%60oc%3D0%60ps%3Dtab05navbar06%60jc%3Dreal_2045&src_module=topcat&src_tab_page_id=page_goods_detail1667596130841&mallCode=1&scici=navbar_MenHomePage~~tab05navbar06~~6~~real_2045~~~~0",
    "https://us.shein.com/ROMWE-Guys-Letter-Wings-Graphic-Drawstring-Sweatpants-p-11698533-cat-2988.html?src_identifier=fc%3DMen%60sc%3DBOTTOMS%60tc%3D0%60oc%3D0%60ps%3Dtab05navbar06%60jc%3Dreal_2045&src_module=topcat&src_tab_page_id=page_goods_detail1667596130841&mallCode=1&scici=navbar_MenHomePage~~tab05navbar06~~6~~real_2045~~~~0"
    "https://us.shein.com/ROMWE-Guys-Lightning-Graphic-Drawstring-Shorts-p-2798518-cat-1976.html?src_identifier=fc%3DMen%60sc%3DBOTTOMS%60tc%3D0%60oc%3D0%60ps%3Dtab05navbar06%60jc%3Dreal_2045&src_module=topcat&src_tab_page_id=page_goods_detail1667596130841&mallCode=1&scici=navbar_MenHomePage~~tab05navbar06~~6~~real_2045~~~~0"
]

# Initialize products
def initjokes():
    # setup products into a dictionary with id, product, good, bad
    item_id = 0
    for item in product_list:
        products_data.append({"id": item_id, "product": item, "good": 0, "bad": 0})
        item_id += 1
    # prime some good responses
    for i in range(10):
        id = getRandomproduct()['id']
        addproductgood(id)
    # prime some good responses
    for i in range(5):
        id = getRandomproduct()['id']
        addproductbad(id)
        
# Return all products from products_data
def getproducts():
    return(products_data)

# product getter
def getproduct(id):
    return(products_data[id])

# Return random product from products_data
def getRandomproduct():
    return(random.choice(products_data))

# Liked product
def favoriteproduct():
    best = 0
    bestID = -1
    for product in getproducts():
        if product['good'] > best:
            best = product['good']
            bestID = product['id']
    return products_data[bestID]
    
# Jeered product
def jeeredproduct():
    worst = 0
    worstID = -1
    for product in getproducts():
        if product['bad'] > worst:
            worst = product['bad']
            worstID = product['id']
    return products_data[worstID]

# Add to good for requested id
def addproductgood(id):
    products_data[id]['good'] = products_data[id]['good'] + 1
    return products_data[id]['good']

# Add to bad for requested id
def addproductbad(id):
    products_data[id]['bad'] = products_data[id]['bad'] + 1
    return products_data[id]['bad']

# Pretty Print product
def printproduct(product):
    print(product['id'], product['product'], "\n", "good:", product['good'], "\n", "bad:", product['bad'], "\n")

# Number of products
def countproducts():
    return len(products_data)

# Test product Model
if __name__ == "__main__": 
    initproducts()  # initialize products
    
    # Most likes and most jeered
    best = favoriteproduct()
    print("Most liked", best['good'])
    printproduct(best)
    worst = jeeredproduct()
    print("Most jeered", worst['bad'])
    printproduct(worst)
    
    # Random product
    print("Random product")
    printproduct(getRandomproduct())
    
    # Count of products
    print("products Count: " + str(countproducts()))