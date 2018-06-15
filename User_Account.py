import getpass, json, random, string, binascii, bcrypt
from Device_Connectivity import NetworkConnection
from Detect_Device import DeviceArchitecture

class UserAccount:
    
    #Main function for account creation
    def account(self):
        
        #Opening JSON file which holds usernames, hashed passwords and associated salts
        try:
            with open("data.json", "r") as inFile:
                self.database = json.load(inFile)
            inFile.close()
        except:
            pass

        #Code block invoking login or account creation
        while True:
            invoke = str(input("New user or login (nu/l/x/d): "))

            #If new user command invoked
            if invoke.lower() == "nu":
                #Storing new username
                user = str(input("Enter username: "))
                #Using getpass to obfuscate password input to interpreter
                uInput = str.encode(getpass.getpass("Enter password: "))

                #Generating new random salt value
                slt = self.saltValue()
                
                #Salting and hashing password
                passOne = self.hashValues(uInput, slt)               

                #Requesting user to re-enter same password again
                uInputTwo = str.encode(getpass.getpass("Enter password again: "))

                #Hashing and salting second password input
                passTwo = self.hashValues(uInputTwo, slt)

                #Checking if username is already taken
                if user in self.database:
                    print("Username already exists, please use different username")
                    pass
                
                #Checking if both passwords entered match
                elif passOne == passTwo:
                    print("Passwords match")
                    #Adding hashed password and salt to dictionary assigned to username as key
                    self.database[user]= [passTwo, slt.decode('ascii')]

                    #Printing database for testing purposes
                    "print(self.database)"

                    #Opening and writing new username and hashed password to JSON out file
                    with open("data.json", "w") as outFile:
                        json.dump(self.database, outFile)
                    outFile.close()

                #Passwords dont match return to initial state   
                else:
                    print("Passwords dont match")                    

            #If login command invoked
            elif invoke.lower() == "l":                

                #Requesting user input username and password and storing values to variables
                user = str(input("Enter username: "))
                uInput = str.encode(getpass.getpass("Enter password: "))
                
                #Authenticate username is in database and hashed and salted password value is assigned to particular username
                if user in self.database:
                    #Extracting original salt associated with username
                    uSlt = self.database[user][1]
                    #Encoding associated salt into binary
                    uSlt = str.encode(uSlt)
                    #Hashing and salting password for user to login
                    passW = self.hashValues(uInput, uSlt)

                    #Verifying hashed and salted password input same as hashed salted password in database
                    if passW == self.database[user][0]:
                        print("Login successful!\nwelcome %s" % (user))                        
                        #Getting host IP after successful user account authentication
                        self.ip = NetworkConnection.device_status()
                        self.device = DeviceArchitecture.system_architecture()
                        print("IP: %s\nOS: %s" % (self.ip, self.device))                    
                else:
                    print("incorrect username or password combination")

            #Command used for exiting program        
            elif invoke.lower() == "x":
                break

            #Command used for testing purposes - prints out current dictionary of usernames and hashed passwords
            elif invoke.lower() == "d":
                print(self.database)
    
    #Funtion for hashing and salting
    def hashValues(self, value, salt):        
        #Encoding salt from string to binary
        hashVal = bcrypt.kdf(value, salt, 128, 16)

        #Generating hex value from binary hash
        key = binascii.hexlify(hashVal)
        
        #Returning decoded hex value
        return key.decode('ascii')

    #Function for generating semi-random salt values
    def saltValue(self):
        #Utilising bcrypt to generate random salt values
        slt = bcrypt.gensalt(20)

        return slt
    
    def main(self):
        self.database = {}       
        self.account()

if __name__ == "__main__":
    Account = UserAccount()
    Account.main()
