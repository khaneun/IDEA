#! /usr/bin/env python
# XCoin API-call sample script (for Python 3.X)
#
# @author	btckorea
# @date	2017-04-11
#
#
# First, Build and install pycurl with the following commands::
# (if necessary, become root)
#
# https://pypi.python.org/pypi/pycurl/7.43.0#downloads
#
# tar xvfz pycurl-7.43.0.tar.gz
# cd pycurl-7.43.0
# python setup.py --libcurl-dll=libcurl.so install
# python setup.py --with-openssl install
# python setup.py install

from core.xcoin_api_client import *

def get_balance(api_key, api_secret, currency="ALL"):
    api = XCoinAPI(api_key, api_secret)

    rgParams = {
        'endpoint': '/info/balance',
        "currency": currency
    }

    result = api.xcoinApiCall(rgParams['endpoint'], rgParams)
    return result

