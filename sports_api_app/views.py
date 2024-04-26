from django.shortcuts import render
import http.client

# Create your views here.
import requests
import http.client
#from .models import SportLeagueData1

from .models import sportsData


def hello():
    render('','hello.html')

def sportsdata(request):
    
    url = "https://v3.football.api-sports.io/leagues"

    payload={}
    headers = {
        'x-rapidapi-key': '0133857b618e4b05c4312a0561fdba81',
        'x-rapidapi-host': 'v3.football.api-sports.io'
    }

    response = requests.request("GET", url, headers=headers, data=payload)
    response_data = response.json()
    print("All data saved successfully.")
    print(type(response_data))
    #print("response::::,,",response_data.response)
    #print(response_data["response"])
    for item in response_data["response"]:
        print("ii:::",item["league"]["id"])
        league_id = item["league"]["id"]
        league_name = item["league"]["name"]
        league_type = item["league"]["type"]
        league_country = item["country"]["name"]
        league_season_year = item["seasons"][0]["year"]
        league_season_start = item["seasons"][0]["start"]
        league_season_end = item["seasons"][0]["end"]

        obj = sportsData(league_id = league_id,league_name = league_name,league_type = league_type,league_country = league_country,league_season_year = league_season_year,league_season_end = league_season_end)
        obj.save()
    return render(request, 'sportsData.html', {'response_data':response_data})
   

def display(request):
    response_data = [
        {'id': 1, 'name': 'John Doe', 'email': 'john@example.com'},
        {'id': 2, 'name': 'Jane Smith', 'email': 'jane@example.com'},
        {'id': 3, 'name': 'Alice Johnson', 'email': 'alice@example.com'}
    ]
    return render(request, 'display.html', {'response_data': response_data})
   
   