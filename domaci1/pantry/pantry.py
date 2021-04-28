import requests

basket = {
    "id":"bg9023",
    "ime":"Nikola",
    "prezime":"Nikolic",
    "smer":"rm",
    "predmeti":["primenjeni distribuirani sistemi", "uvod u programiranje", "matematicka analiza"],
    "prosek":10.0,
    "kontakt":{
        "adresa":"Bulevar Nikole Tesle",
        "mesto":"Beograd",
        "telefon":0657723329
    }
}

url = "https://getpantry.cloud/apiv1/pantry/3a0049c2-3f12-4e43-880c-00f45b5370e2/basket/pantry_test" 

post_basket = requests.post(url, json=basket)

