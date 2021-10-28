def compare(field1,field2):
    '''Merge if both are equal'''
    if((field1 is not None) and (field2 is not None) and (field1 == field2)):
        return field1,None
    else:
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
    pincode=None,
    **data
):
    '''Algorithm to simplify address fields'''
    
    locality,landmark = compare(locality,landmark)
    village,subdistrict = compare(village,subdistrict)
    if(subdistrict is not None):
        subdistrict,district = compare(subdistrict,district)
    if(district is not None):
        district,state = compare(district,state)
    

    input_data = [house, street, locality, landmark, village, subdistrict, district, state, pincode]
    for i in range(len(input_data)):
        if(input_data[i] is None):
            input_data[i] = 'NA'
        
    
    input_data = list(map(str,input_data))
    address = ", ".join(input_data)
    return address
if __name__ == '__main__':
    # for i in ['one','two',None]:
    #     for j in ['one','two',None]:
    #         print(i,j,compare(i,j))
    print(simplify("one","two","three","three","five","five","eight","eight","nine"))


