from django.shortcuts import render
from django.conf import settings
import requests 
# Create your views here.



# Define the home view
def home(request):
  #access and assign fields from the form on the homepage
  #pushing user info into a list on klaviyo 
  name = request.POST.get("name", '')
  email = request.POST.get("email", '')  
  number = request.POST.get("phone_number", '')
  #access hidden list id and api key   
  list = settings.LIST_ID
  api_key = settings.API_KEY
  url = f"https://a.klaviyo.com/api/v2/list/{list}/subscribe"
  PARAMS = {'api_key': api_key}
  
  payload = {"profiles": [{
                        "name": name, 
                        "email": email,
                        "phone_number": number,
                        "sms_consent": True
}]} 

  headers = {
    "Accept": "application/json",
    "Content-Type": "application/json"
}

  response = requests.post(url=url, params=PARAMS, json=payload, headers=headers)
  #push the response to html page to show any error on the post request
  res = response.json()
  print(payload)
  return render(request, 'home.html', {'res': res})



def list(request):
  #another api call for the user to ensure they are working with the correct list and check
  #when the last time the list was updated
  #access hidden api key and list id 
  list = settings.LIST_ID
  api_key = settings.API_KEY
  url = f"https://a.klaviyo.com/api/v2/list/{list}"
  PARAMS = {'api_key': api_key}

  headers = {"Accept": "application/json"}

  response = requests.get(url, params=PARAMS, headers=headers)
  #pushing response through to display necessary info on the list page 
  res = response.json()
  print(response.text)
  return render(request, 'list.html', {'res': res})
