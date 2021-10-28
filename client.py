import requests
res = requests.post('https://7b2a-2409-4070-2d4a-7b3d-c4f8-c563-911d-e403.ngrok.io',json={
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