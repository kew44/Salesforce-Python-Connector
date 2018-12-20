from SFConnector import SalesforceConnector

if __name__ == '__main__':
    SFOb1 = SalesforceConnector('sona@test.com','VictorHoney1',"")
    SFOb1.SFLogIn()
    print("Logged to salesforce successfully")
    SFOb1.createContact("Amala","akhila@gmail.com")