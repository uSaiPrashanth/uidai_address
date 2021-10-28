def compare(field1,field2):
    '''Merge if both are equal'''
    if((field1 is not None) and (field2 is not None)):
        if(field1 == field2):
            return field1,"NA"
        else:
            return field1,field2
    if(field1 is None):
        field1 = "NA"
    if(field2 is None):
        field2 = "NA"
    return field1,field2

def simplify(
    house=None,
    street=None,
    locality=None,
    landmark=None,
    village=None,
    subdistrict=None,
    district=None,
    state=None,
    pincode=None
):
    '''Algorithm to simplify address fields'''
    locality,landmark = compare(locality,landmark)
    village,subdistrict = compare(village,subdistrict)
    if(subdistrict != "NA"):
        subdistrict,district = compare(subdistrict,district)
    if(district != "NA"):
        district,state = compare(district,state)
    print([house, street, locality,
        landmark, village, subdistrict,
        district, state, pincode])
    address = " ".join(
        [house, street, locality,
        landmark, village, subdistrict,
        district, state, pincode]
    return address
if __name__ == '__main__':
    for i in ['one','two',None]:
        for j in ['one','two',None]:
            print(i,j,compare(i,j))
    print(simplify())


