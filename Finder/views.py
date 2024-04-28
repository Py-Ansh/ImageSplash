from django.shortcuts import render, HttpResponse
from Finder.models import Contact
from datetime import datetime

import requests

from django.contrib import messages

# Create your views here.

def index(request):
	return render(request, "index.html")



def contact(request):
	if request.method == "POST":
		email = request.POST.get("email")
		suggestions = request.POST.get("suggestions")

		contact = Contact(email=email, suggestions=suggestions, date=datetime.today())
		contact.save()

		messages.success(request, "Your Message has been sent")



	return render(request, "contact.html")




def search(request):
    if request.method == "GET":
        name = request.GET.get("name")
        quality = request.GET.get("quality")

        num_images = 6
	    
        # Initialize a list to store photo URLs
        photo_urls = []
        p_names = []

        # Make multiple requests to the Unsplash API to get random photos based on your parameters
        for _ in range(num_images):
            unsplash_api_url = f"https://api.unsplash.com/photos/random/?query={name}&client_id=kJ2KK2kq6YanDhocvnHyiT6JItmmQJgsbpgFW_jFWHk"
            # unsplash_api_url = f"https://api.unsplash.com/photos/random/?query={name}"

            response = requests.get(unsplash_api_url)
	        
            if response.status_code == 200:
                # Parse the response JSON to access the photo URL
                photo_data = response.json()
                photo_url = photo_data.get('urls', {}).get(quality)

                photographer_name = photo_data['user']['name']

                if photo_url:
                    photo_urls.append(photo_url)
                    p_names.append(photographer_name)

	    
        context = {'photo_urls': photo_urls, 'photographer' : p_names}
        print(context)


        return render(request, "searching.html", context=context)

    return HttpResponse("404")

