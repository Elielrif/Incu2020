import pymongo

url = 'mongodb://svetlana:cisco123@localhost:27017/Device_Configuration'
with pymongo.MongoClient(url) as client:
    db = client.Device_Configuration
    collection = db.Interfaces

    collection.insert_one({
            'Switch_name': 'bru-dna-1',
            'Interface_Name': 'g1/0',
            'Description': "Connected to the switch2 gi1/2",
            'state': "up"
        })
    collection.insert_one({
            'Switch_name': 'bru-dna-1',
            'Interface_Name': 'fc1/1/0',
            'Description': "connected to the storage port 1",
            'state': "up"
        })
    collection.insert_one({
            'Switch_name': 'mastodon',
            'Interface_Name': 'GigabitEthernet1/0/3 ',
            'Description': "Connected to printer CX2",
            'state': "up"
        })
    collection.insert_one({
            'Switch_name': 'mastodon',
            'Interface_Name': 'GigabitEthernet1/0/5 ',
            'Description': "Connected to printer CX4",
            'state': "down"
        })
    collection.insert_one({
            'Switch_name': 'mastodon',
            'Interface_Name': 'GigabitEthernet1/4/3 ',
            'Description': "Connected to server SERV1",
            'state': "up"
        })




