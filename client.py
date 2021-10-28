import requests

fields = [
    'house',
    'street',
    'locality',
    'landmark',
    'village',
    'subdistrict',
    'district',
    'state',
    'pincode'
]

if __name__=='__main__':
    address_dict = {}

    print("Enter your data for the following fields. Enter NA if not applicable")
    for i in fields:
        val = input(f'Enter your {i} address:')
        if(val.lower() == 'na'):
            val = None
        address_dict[i] = val 

    res = requests.post('http://127.0.0.1:5000/',json=address_dict)

    if(res.ok):
        print(f'The address you have entered is: { res.json()["address"] }')