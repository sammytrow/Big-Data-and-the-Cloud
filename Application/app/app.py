from flask import Flask, request, jsonify

from app.content.run_example import *

app = Flask(__name__)


@app.route('/')
def main(): # put application's code here
    #AreaID, CrownpassID, EntryDate, EntryTime, ExitDate, ExitTime
    #input("Press Enter to continue... (example_login_")
    #example_login()
    #input("Press Enter to continue... (example_staff_login)")
    #example_staff_login()
    #input("Press Enter to continue... (example_registration)")
    area = example_registration()
    print(area)
    #input("Press Enter to continue... (example_login)")
    print(example_login())
    #input("Press Enter to continue... (example_staff_reg)")
    area.staff.append(example_staff_reg(area))
    print(area.staff)
    #input("Press Enter to continue... (example_staff_login)")
    print(example_staff_login())
    #input("Press Enter to continue... (example_checkin)")
    print(example_checkin())
    #input("Press Enter to continue... (example_checkout)")
    print(example_checkout())
    return 'Hello World!'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
