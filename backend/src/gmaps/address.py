import requests
from geopy.geocoders import Nominatim


def geocode_address(address):
    geolocator = Nominatim(user_agent="myapp")  # Specify a unique user agent
    location = geolocator.geocode(address)
    if location:
        return location.latitude, location.longitude
    else:
        return None
    

def gmaps(address):
    query = 'hospitals|clinics'
    latitude, longitude = geocode_address(address)
    link = f'https://serpapi.com/search.json?engine=google_maps&q={query}&ll=@{latitude},{longitude},15.1z&type=search'
    params = {
    'key':'a417c75840f5b0aabab2ffdf6f0ee103e072bad3a9182c0fef468cf534772362',
    }
    response = requests.get(link, params=params)
    addresses = dict(response.json())
    hospitals = addresses['local_results']
    
    hospital_data = []
    
    for i in range(len(hospitals)):        
        try:title = (hospitals[i]['title']).strip()
        except:title = ('Not Specified')
        
        try:address = (hospitals[i]['address']).strip()
        except:address = ('Not Specified')
            
        try:operating_days = ([days for days in hospitals[i]['operating_hours']])
        except:operating_days = ('Not Specified')
        
        try:open_hours = (hospitals[i]['open_state'])
        except:open_hours = ('Not Specified')
            
        try:phone = (hospitals[i]['phone'])
        except:phone = ('Not Specified')
            
        try:type = (hospitals[i]['type'])
        except:type = ('Not Specified')
        
        try:reviews = (hospitals[i]['reviews'])
        except:reviews = ('Not Specified')
        
        try:rating = (hospitals[i]['rating'])
        except:rating = ('Not Specified')
            
        try:thumbnail = (hospitals[i]['thumbnail'])
        except:thumbnail = ('Not Specified')
        
        
        data = {
        'hospital_id':i,
        'name':title,
        'address':address,
        'days_open':operating_days,
        'open_time':open_hours,
        'contact': phone,
        'disease_treatment_type':type,
        'reviews':reviews,
        'rating': rating,
        'image':thumbnail,
        }
        
        hospital_data.append(data)
        

    return hospital_data


if __name__=='__main__':

    address = "sagarshet, maharashtra, india"
    hospoital_data = gmaps(address)
    # print(hospoital_data)
