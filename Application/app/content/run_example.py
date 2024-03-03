from app.content.EntryManagement import check_in, check_out
from app.content.OwnerManagement import AreaAccount
from app.content.StaffManagement import StaffAccount

'''
    pip install Flask
    pip install opencv-python qrcode numpy --user
    pip install datetime
    pip install 'pymongo[srv]'
'''

area_example = {'password' : 'test_password', 'areaName' : 'The Four Candles - JD Wetherspoon', 'username' : '4candles','postcode' : 'OX4 3LR', 'county' : 'Oxfordshire',
                'city' : 'Oxford', 'street' : 'Between Towns Rd', 'areaNum' : '59a', 'entryLvl' : '2', 'maxNum' : '50'}
staff_example = {'username' : 'staff1', 'password' : 'test_password1'}

def example_registration():
    area = AreaAccount()
    result = area.register(area_example)
    print(result)
    return area


def example_login():
    area = AreaAccount()
    result = area.login(area_example["username"], area_example["password"])
    print(result)

def example_staff_reg(area):
    new_staff = StaffAccount()
    result = new_staff.register(staff_example, area.areaID)
    print(result)
    return new_staff

def example_staff_login():
    staff = StaffAccount()
    result = staff.login(staff_example["username"], staff_example["password"])
    print(result)

def example_checkin():
    response = check_in("07c51711-777d-48d4-a240-94c227bf2e49")
    print(response)
    response = check_in("c92ce37c-650e-479d-b94f-c9d86cfb198c")
    print(response)

def example_checkout():
    response = check_out("c92ce37c-650e-479d-b94f-c9d86cfb198c")
    print(response)

