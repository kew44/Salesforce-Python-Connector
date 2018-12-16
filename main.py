#! /usr/bin/env python3

from simple_salesforce import Salesforce

__version__ = '1.0.0'

class SFConnect():
    def __init__(self):
        print("inside init")

def main():
    print("Hello world")
    sf = Salesforce(username='test@test.com', password='password', security_token='')
    print(sf.query("SELECT Id, Email FROM Contact LIMIT 5"))



if __name__ == "__main__": main()