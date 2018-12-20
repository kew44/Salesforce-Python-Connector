from simple_salesforce import Salesforce


class SalesforceConnector():

    def __init__(self,username,password,token):

        self.username = username
        self.password = password
        self.token = token
    
    def SFLogIn(self):
        try:
            print("here")

            self.sf  = Salesforce(username=self.username, password=self.password, security_token=self.token)
            print("here")
        except Exception as e:
            print("One field is missing"+e)

    def createContact(self,LastName,Email):
        try:
            self.LastName = LastName
            self.Email = Email
            self.sf.Contact.create({'LastName':self.LastName,'Email':self.Email})
        except Exception as e:
            print("Exception occured"+e)


