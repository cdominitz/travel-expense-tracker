# Microservice Implementation
# Programmers: Kaitlyn Hornbuckle
# Date: May 8, 2022
# The code below is adapted from the Exchangerate.host API:
# https://exchangerate.host/#/docs
# This is part of a microservice that allows users to convert one type of
#   currency to another.
# The final calculation is written to a text file named "curr_calculation.txt."
#   This is
# one of the main communication pipes that will need to be used when
#   implemented in a separate program.

import requests
import json


def convert(info):
    """
    Reads currency parameters from text file
    #1. Home currency
    #2. Foreign currency
    #3. Amount (integers or floats only)"""

    home_code = info[0]
    conv_code = info[1]
    amount = info[2]

#   Converts the requested currency and returns the result
    inputStr = "https://api.exchangerate.host/convert?from=" + str(home_code)\
               + "&to=" + str(conv_code) + "&amount=" + str(amount)

    url = inputStr
    response = requests.get(url)
    data = response.json()

    jsonObj = json.dumps(data)
    conversion = json.loads(jsonObj)

    return conversion["result"]
