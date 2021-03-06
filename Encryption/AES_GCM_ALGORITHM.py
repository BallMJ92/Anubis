import json, time, datetime
from timeit import default_timer as timer
from base64 import b64encode
from base64 import b64decode
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

class AES_GCM_ALGORITHM:

    def __init__(self,):
        #Initialising timestamp variable
        self.timestamp = (datetime.datetime.fromtimestamp(time.time())
                            .strftime("%Y-%m-%d %H:%M:%S"))        
        #Initalising new symmetric key with 32 byte keyspace
        self.key = get_random_bytes(32)
        

    def GCM_Encryption(self, header, data):       
        try:
            #Generating new AES cipher in GCM mode using 32 byte key
            cipher = AES.new(self.key, AES.MODE_GCM)
            #Adding header to cipher
            cipher.update(header)
            #Encrypting data
            ciphertext, tag = cipher.encrypt_and_digest(data)
            #Saving constituent parts into JSON database
            json_output = self.JSON_Output(cipher, header, ciphertext, tag)
        except Exception as inst:
            print(type(inst))
            print(inst.args)
            print(inst)
        finally:
            #Returning database
            return json_output       

    def GCM_Decryption(self):
        try:
            #Opening JSON database
            b64 = self.JSON_Open_Database()
            json_k = ["nonce", "header", "ciphertext", "tag"]
            #Initialising new dictionary containing values from database
            jv = {k:b64decode(b64[k]) for k in (json_k)}
            cipher = AES.new(self.key, AES.MODE_GCM, nonce = jv["nonce"])
            cipher.update(jv["header"])
            plaintext = cipher.decrypt_and_verify(jv["ciphertext"], jv["tag"])        
        except Exception as inst:
            print(type(inst))
            print(inst.args)
            print(inst)
        finally:
            return plaintext.decode("utf-8")

    def JSON_Open_Database(self):
        #Opening and returning database values
        try:
            with open("data.json", "r") as inFile:
                database = json.load(inFile)
            inFile.close()
        except Exception as inst:
            print(type(inst))
            print(inst.args)
            print(inst)      
        finally:
            return database

    def JSON_Save_Database(self, json_k, json_v):
        #writing json k and v into database
        result_dump = json.dumps(dict(zip(json_k, json_v)))
        with open("data.json", "w") as outFile:
            #Converting and zipping variables into dictionary
            json.dump(dict(zip(json_k, json_v)), outFile)
        outFile.close()

        return result_dump

    def JSON_Output(self, cipher, header, ciphertext, tag):
        #Initialising database output dictionary keys and encoded corresponding values
        json_k = ["nonce", "header", "ciphertext", "tag"]
        json_v = [b64encode(x).decode('utf-8') for x in (cipher.nonce, header, ciphertext, tag)]
        key_dump = self.JSON_Save_Database(json_k, json_v)
        
        return key_dump

    #Function for running and testing encryption and decryption functions individually
    def Algorithm_Test(self):
        pHeader = b"Test"
        pData = b"T"

        #Executing encryption function
        try:            
            s1 = timer()
            print(self.GCM_Encryption(pHeader, pData), "\n----------")
            e1 = timer()
            print("Encryption execution speed: %d\n" % (e1-s1))
        except Exception as inst:
            print(type(inst))
            print(inst.args)
            print(inst)
        finally:
            True

        #Executing decryption function
        try:
            s2 = timer()
            print(self.GCM_Decryption(), "\n----------")
            e2 = timer()
            print("Decryption execution speed: %d" % (e2-s2))
        except Exception as inst:
            print(type(inst))
            print(inst.args)
            print(inst)
        finally:
            True

    def main(self):
        self.Algorithm_Test()


if __name__ == "__main__":
    AESGCM = AES_GCM_ALGORITHM()
    AESGCM.main()




