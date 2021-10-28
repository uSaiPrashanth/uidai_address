import requests
res = requests.post('http://127.0.0.1:5000/',json={
    'house':'B-102 Sri Shiridi Sai Enclave',
    'street':'Street no 9',
    'locality':'Gayathri Nagar',
    'landmark':'Near Xavior School',
    'village':None,
    'subdistrict':'Medchel',
    'district':'Hyderabad',
    'state':'Telangana',
    'pincode':500040
})
if(res.ok):
    print(res.json()['address'])