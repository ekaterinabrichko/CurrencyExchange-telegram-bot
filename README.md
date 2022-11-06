# Telegram bot for Currency exchange

This bot returns the price for a certain amount of currency: dollar, euro, Belarusian ruble, zloty or hryvnia.

To create a bot the following libraries are used:
- pytelegrambotapi
- JSON library


# **Bot workflow**
1. User enters **/start** command: welcome message is displayed, where user needs to click or enter **/help** command to see further instructions.
2. User clicks or enters **/currencies** command to see information on all available currencies to use.
3. To get results user types in message in the following format: 'name of the currency to be exchanged' 'name of the currency of interest' 'amount of the 1st currency'


To take the exchange rate, you need to use the API and send requests to it using the Requests library. If the user makes a mistake (for example, an incorrect or non-existent currency is entered), throw custom APIException with the text explaining the error. The text of any error indicates the type of error which is sent to the user in the message.

To send requests to the API, describe a class with a static get_price() method that takes three arguments: the name of the currency you want to know the price of - base, the name of the currency you want to know the price in - quote, the amount of the transferred currency - amount and returns desired amount in currency. Store the telegram bot token in a special config (you can use a .py file). Hide all classes in the extensions.py file.
