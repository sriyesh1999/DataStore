import os
import json
import time
import sys
from threading import Lock


class DataStore:

    def __init__(self,filepath=os.getcwd()):
        self.lock = Lock()
        if self.verifypath(filepath):
            self.filepath=os.path.join(filepath,'db.json')
            created =self.filecreation(self.filepath)

            if created ==1:
                if os.stat(self.filepath).st_size != 0:
                    file = open(self.filepath, 'r')

                    self.data = json.load(file)
                    file.close()
                else:
                    self.data = {}
            else:
                file = open(self.filepath, 'w')
                file.close()
                self.data = {}
        else:
            self.filepath()

    def Size(self):

        if os.path.getsize(self.filepath) <= 1024**3:
            return False
        else:
            return True

    def create(self,key,value,time_to_live=0):

        with self.lock:                                                  #For thread Safety
            try:
                if self.Size():
                    raise Exception("File size is 1 GB ,cannot add more data")
                if type(key)!=int:
                    if key == "" or len(key) >32 :
                        raise Exception("Invalid key Input")
                if type(key)==int:
                    raise Exception("Enter String")
                if self.data:
                    if key in self.data.keys():
                        raise Exception("Key is already Present")
                try:
                    value=json.loads(value)
                except:
                    raise Exception("Enter correct json format")



                if sys.getsizeof(value) > 16 * 1000:
                    raise Exception("Size of the value exceeds 16KB size limit")
                if time_to_live!=0:
                    time_to_live=int(time.time())+ abs(int(time_to_live))
                    d={"value":value,"time_to_live":time_to_live}

                else:
                    d={"value":value}
                self.data[key]=d
                f=open(self.filepath,'w')
                json.dump(self.data,fp=f,indent=2)
                f.close()
                return ("Value Added")
            except Exception as e:
                return (e)
    def read(self,key):
        with self.lock:
            try:
                if self.data != {}:
                    if key in self.data:
                        try:
                            if time.time() > self.data[key]["time_to_live"]:
                                raise Exception("Key-value pair time to live has expired,Unable to read")
                            else:
                                return (self.data[key]["value"])

                        except KeyError:
                            return (self.data[key]["value"])
                    else:
                        raise Exception("Key not found")
                else:
                    raise Exception("Empty File")
            except Exception as e:
                return (e)

    def delete(self,key):
        with self.lock:
            try:
                if self.data:
                    if key in self.data:
                        flag = 0
                        try:
                            if time.time() > self.data[key]["time_to_live"]:
                                raise Exception("Key-value pair  time to live has expired,Unable to delete")
                                flag = 1
                            else:
                                del self.data[key]
                        except KeyError:
                            del self.data[key]

                        if self.data == {}:
                            os.remove(self.filepath)

                        else:
                            f = open(self.filepath, 'w')
                            json.dump(self.data, f)
                            f.close()

                        if flag == 0:
                            return ("Deleted")
                    else:
                        raise Exception("Key not found")
                else:
                    raise Exception(" Empty File")
            except Exception as e:
                return (e)

    @staticmethod
    def filepath():
        print("Wrong File Path")
        exit()

    @staticmethod
    def verifypath(filepath):
        if os.path.exists(filepath):
            return True
        return False

    @staticmethod
    def filecreation(filepath):
        if os.path.exists(filepath):
            print("File Selected")
            created = 1
        else:
            print("File Created")
            created = 0
        return created

























