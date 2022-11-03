import requests, json


user_input = input("Enter article of clothing: ")

url = "https://pricer.p.rapidapi.com/str"

querystring = {"q":user_input}

headers = {
	"X-RapidAPI-Key": "cbb692713amshcff277d5ed43230p18a579jsn38813b83b73b",
	"X-RapidAPI-Host": "pricer.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)

y = json.loads(response.text)

# print(y[0]["title"])

# parsing the Json to make it easier for the frontend 
# defining my variables for user input 
title = (y[0]["title"])
price = (y[0]["price"])
shop = (y[0]["shop"])
shipping = (y[0]["shipping"])
link = (y[0]["link"])
image = (y[0]["img"])

print(title)
print(price)
print(shop)
print(shipping)
print(link)
print(image)