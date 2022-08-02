# SMS Subscription Feeder

### Description
This solution is designed to enable users to add profiles to their Klaviyo sms subscription list. Using the Klaviyo 'Subscribe Profiles to List' API, users can instantly subscribe users to their SMS Subscribers list without having to log into their account and navigate to the list. Users can also verify that the solution is linked to the correct list by visiting the 'list' page. This page uses Klaviyo's 'Get List Info' API call and reveals the name and date last updated of the list id being used by the solution. 

### Technology Used
Python, Django, HTML, Klaviyo APIs

### How to run locally
1. Clone down this repository to your computer and go to the new directory in your terminal
2. Create a django virtual environment and run (this video is helpful https://www.youtube.com/watch?v=PS903MeNDJk)
    - While in the terminal run "python -m venv django-env"
    - Then run source bin/activate to activate the terminal
