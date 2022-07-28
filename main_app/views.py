from django.shortcuts import render
from django.conf import settings
import requests 
# Create your views here.
# Add the following import
from django.http import HttpResponse

# Define the home view
def home(request):
  name = request.POST.get("name", '')
  email = request.POST.get("email", '')  
  number = request.POST.get("phone_number", '')  

  api_key = settings.API_KEY
  url = "https://a.klaviyo.com/api/v2/list/W98kVN/subscribe"
  PARAMS = {'api_key': api_key}
  
  payload = {"profiles": [{"name": name, 
                        "email": email,
                        "phone_number": number,
                        "sms_consent": True
}]} 



  headers = {
    "Accept": "application/json",
    "Content-Type": "application/json"
}

  response = requests.post(url=url, params=PARAMS, json=payload, headers=headers)
  res = response.json()
  print(payload)
  return render(request, 'home.html', {'res': res},)

