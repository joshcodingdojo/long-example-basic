from django.shortcuts import render, redirect
import requests
API_KEY = 'AIzaSyB_dNuh4Q4bd-ns_mdfWMX1_HeodQZFJzk'

# Create your views here.
def index(request):
  return render(request, "index.html")

def view_officials(request):
  if request.method == "POST":
    zipcode = request.POST['zipcode']
    response = requests.get(f"https://www.googleapis.com/civicinfo/v2/representatives?key={API_KEY}&address={zipcode}&includeOffices=true")
    json = response.json()
    offices = json['offices']
    officials = json['officials']
    # add elected office to officials
    for i in offices:
      for j in i['officialIndices']:
        officials[j]['elected_office'] = i['name']
    context = {
      "officials": officials
    }
    request.session['officials'] = officials
    return redirect('/show-officials')

def show_officials(request):
  context = {
    "officials": request.session['officials']
  }
  return render(request, 'show_officials.html', context)

def rate_official(request, name, elected_office):
  print('User wants to rate', name, elected_office)
  context = {
    "official_name": name,
    "elected_office": elected_office
  }
  return render(request, 'rate.html', context)