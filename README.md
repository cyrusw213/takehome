# SMS Subscription Feeder

### Description
This solution is designed to enable users to add profiles to their Klaviyo sms subscription list. Using the Klaviyo 'Subscribe Profiles to List' API, users can instantly subscribe users to their SMS Subscribers list without having to log into their account and navigate to the list. Users can also verify that the solution is linked to the correct list by visiting the 'list' page. This page uses Klaviyo's 'Get List Info' API call and reveals the name and date last updated of the list id being used by the solution. 

### Technology Used
Python, Django, HTML, Klaviyo APIs

### How to run locally
1. Clone down this repository to your computer and go to the new directory in your terminal
2. Create a django virtual environment and run it (this [video](https://www.youtube.com/watch?v=PS903MeNDJk) is helpful)
    - While in the terminal run "python3 -m venv django-env" 
    - run "cd django-env"
    - Then run "source bin/activate" to activate the terminal
    - If succesful (django-env) will appear before the command line prompt
3. Move to the main app's directory (takehome)
4. install requirements (run "pip install -r requirements.txt")
5. Create a file named .env (touch .env)
 add the following to your .env file:
    - SECRET_KEY= create your own secret key (recommend this [site](https://miniwebtool.com/django-secret-key-generator/))
    - API_KEY= generate a private api key from klaviyo and add it here
    - LIST_ID = this will be the list id for whichever Klaviyo list you want to attach to the solution
6. from the terminal where your virtual environment is running run the following command "python manage.py runserver"
7. You should be able to now add users to your list from your localhost!