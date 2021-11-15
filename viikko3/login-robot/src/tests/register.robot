*** Settings ***
Resource  resource.robot
Test Setup  Input New Command And Create User

*** Test Cases ***
Register With Valid Username And Password
    Input Credentials  pekka  pekka123
    Output Should Contain  New user registered

Register With Already Taken Username And Valid Password
    Input Credentials  kalle  pekka123
    Output Should Contain  User with username kalle already exists

Register With Too Short Username And Valid Password
    Input Credentials  kk  pekka123
    Output Should Contain  Username is too short

Register With Valid Username And Too Short Password
    Input Credentials  pekka  pp55
    Output Should Contain  Password is too short

Register With Valid Username And Long Enough Password Containing Only Letters
    Input Credentials  pekka  pekkayykaakoo
    Output Should Contain  Password should not contain only letters

Register With Username Containing Else Than Letters And Valid Password
    Input Credentials  p3kk4  pekka123
    Output Should Contain  Username should contain only letters

*** Keywords ***
Input New Command And Create User
    Create User  kalle  kalle123
    Input New Command