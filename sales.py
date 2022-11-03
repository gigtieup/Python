import requests

url = "https://pricer.p.rapidapi.com/str"

querystring = {"q":"iphone"}

headers = {
	"X-RapidAPI-Key": "6fa44ed3a2msh483515e3beca32dp153a87jsn04ee72a909e0",
	"X-RapidAPI-Host": "pricer.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)