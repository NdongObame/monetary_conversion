import requests

currencies = {1: "USD",
              2: "XAF",
              3: "EURO",
              4: "ZAR"
              }
print("the available currencies are"
      + "\n" + str(currencies))

choice_1 = input("you want to convert :")
currency_one = currencies[int(choice_1)]

choice_2 = input("into :")
currency_two = currencies[int(choice_2)]

url = 'https://api.exchangerate.host/convert?from=' + currency_one + '&to=' + currency_two
response = requests.get(url)
data = response.json()

exchange_rate = data['result']
amount = input("how many " + currency_one + " do you want to convert into " + currency_two + " :")
conversion = round(float(amount) * float(exchange_rate), 2)
print("you will have " + str(conversion) + " " + currency_two)
