#!/usr/bin/env python3
'''
MIT License

Copyright (c) [year] [fullname]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

__license__ = "Apache2"
__version__ = "0.1.1"
__maintainer__ = "Rick Kauffman"
__status__ = "Alpha"
-------------------------------------------------------------------------------
'''
from requests.packages.urllib3.exceptions import InsecureRequestWarning
import urllib3
import requests
import os
import sys
import logging
import json
import pyafc.session as session
import pyafc.devices as devices
import pyafc.fabric as fabric
import pyafc.vrfs as vrfs
# import pyafc.leafspine as leafspine
import pyafc.ntp as ntp
import pyafc.dns as dns
import vars.vars as vars


urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
logging.basicConfig(level=logging.INFO)


def main():


    # Obtain Session login information
    login_session, auth_header = session.login(vars.base_url, vars.username, vars.password)
    # print(auth_header)
    session_dict = dict(s=login_session, url=vars.base_url)

    try:

        print("Posting a new fabric...")
        response = fabric.create_fabric(vars.fabric_name, auth_header, vars.timezone, vars.fabric_description, **session_dict)
        print('---------------------------------------------------------')
        print(response)



    except Exception as error:
        print('Ran into exception: {}. Logging out...'.format(error))
        session.logout(auth_header, **session_dict)


if __name__ == '__main__':
    main()
