#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pymongo as pymongo

def print_hi(name):
    print(f'Hi, {name}')

def connectbd():
    myclient = pymongo.MongoClient(
        "mongodb+srv://LinhLE:truclinh@cluster0.kkz3d.mongodb.net/test?retryWrites=true&w=majority")
    mydb = myclient["test"]
    #countries = mydb["countries"]
    return mydb
# test is your database name
# list all country OK
def list():
    countries = connectbd()["countries"]
    for country in countries.find():
            print(country['name'])
# Point 1 get all countries where a letter or word given is in the name OK
def number_1():
    countries = connectbd()["countries"]
    letter=input("Enter your word: ")
    myquery = {"name": {"$regex": ".*" + letter + ".*"}}
    document = countries.find(myquery)

    for x in document:
        print(x)
# 2 Add continent collection link to countries collection. Actually Done in NodeJs
#3 Send the list of continent with there number of country OK
def number_3():
    continents = connectbd()["continents"]
    list_continent = continents.aggregate([{'$project': {'name': 1, '_id': 0, 'NumberOfCountries is ': {'$size': '$countries'}}}])
    for x in list_continent:
        print(x)

# Number 4: Gets till the 4th country under specified continent ordered by name
def number_4():
    continents = connectbd()["continents"]
    countries = connectbd()["countries"]
    from bson.objectid import ObjectId
    for continent in continents.find():
        for country_id in continent["countries"]:
            list = countries.find({"_id": ObjectId(country_id)}).sort("name")
            print(continent["name"], ':', list[0]["name"])


#5 insert population into countries OK
def number_5():
    countries = connectbd()["countries"]
    countries.update_many({}, {"$set": {"population":"xyz" }})
    countries.find_one_and_update({'name': "France"},
                                  {'$set': {"population": 67390000}})
    countries.find_one_and_update({'name': "Greece"},
                                        {'$set': {"population": 10720000}})
    countries.find_one_and_update({'name': "Germany"},
                                        {'$set': {"population": 83240000}})
    countries.find_one_and_update({'name': "Italy"},
                                        {'$set': {"population": 59550000}})
    countries.find_one_and_update({'name': "Finland"},
                                        {'$set': {"population": 5531000}})
    countries.find_one_and_update({'name': "China"},
                                        {'$set': {"population": 1400000000}})
    countries.find_one_and_update({'name': "Indonesia"},
                                        {'$set': {"population": 273500000}})
    countries.find_one_and_update({'name': "Vietnam"},
                                        {'$set': {"population": 97340000}})
    countries.find_one_and_update({'name': "IRAN"},
                                        {'$set': {"population": 83990000}})

# 6 Gets all countries ordered by population in ascending order OK
def number_6():
    countries = connectbd()["countries"]
    order=countries.find().sort("population",1)
    for x in order:
        print(x)
# 7 // Number 7: Gets countries where population is greater than 100000 and including u in the country name OK
def number_7():
    countries = connectbd()["countries"]

    x = countries.find({"population": {"$gt": 100000}, "name": {"$regex": "u"}})
    for i in x:
        print(i)

if __name__ == '__main__':
    print_hi('PyCharm')
    connectbd()
    #list()
    #number_1()
    #number_3()
    number_4()
    #number_5()
    #number_6()
    #number_7()









# In[ ]:




