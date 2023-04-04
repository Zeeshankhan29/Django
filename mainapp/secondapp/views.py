from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
import pymongo
import json

def test1(request):
    # client = pymongo.MongoClient("mongodb+srv://mongodb:mongodb@cluster0.gc1mb.mongodb.net/?retryWrites=true&w=majority")
    # dbname = client['Newdatabase']
    # col = dbname['collection']

  
    # result = col.insert_one({'name': 'John', 'age': 27})

    # # Retrieve the document and convert ObjectId to string
    # document = col.find_one({'_id': result.inserted_id})
    # document['_id'] = str(document['_id'])

    # # Serialize the document to JSON and return as response
    # return JsonResponse(document, safe=False)
    return HttpResponse('this is the second try')
