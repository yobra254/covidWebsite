from django.shortcuts import render
import requests
import json

url = "https://covid-193.p.rapidapi.com/statistics"

headers = {
    'x-rapidapi-key': "254bc17ca7msh807893e25f01cafp13dae1jsn59f3f9e4e474",
    'x-rapidapi-host': "covid-193.p.rapidapi.com"
    }

response = requests.request("GET", url, headers=headers).json()



# Create your views here.

def helloworldview(request):
    noofresults= int(response['results'])
    mylist=[]
    for x in range(0, noofresults):
        mylist.append(response['response'][x]['country'])
    context={'mylist': mylist}
    return render(request,'hello.html',context)