*** Settings ***
Resource  resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Create User And Go To Register Page

*** Test Cases ***
Register With Valid Username And Password
    Set Username  pekka
    Set Password  pekka123
    Set Password Confirmation  pekka123
    Submit Credentials
    Register Should Succeed

Register With Too Short Username And Valid Password
    Set Username  pe
    Set Password  pekka123
    Set Password Confirmation  pekka123
    Submit Credentials
    Register Should Fail With Message  Username is too short

Register With Valid Username And Too Short Password
    Set Username  pekka
    Set Password  pe123
    Set Password Confirmation  pe123
    Submit Credentials
    Register Should Fail With Message  Password is too short

Register With Nonmatching Password And Password Confirmation
    Set Username  pekka
    Set Password  pekka123
    Set Password Confirmation  pekka456
    Submit Credentials
    Register Should Fail With Message  Password and confirmation don't match


Register With Nonexisting Password
    Set Username  pekka
    Set Password Confirmation  pekka456
    Submit Credentials
    Register Should Fail With Message  Username and password are required

Register With Ununique Username
    Set Username  kalle
    Set Password  kalle456
    Set Password Confirmation  kalle456
    Submit Credentials
    Register Should Fail With Message  Username must be unique

Login After Successful Registration
    Set Username  maiju
    Set Password  maiju123
    Set Password Confirmation  maiju123
    Submit Credentials
    Register Should Succeed
    Go To Login Page
    Login Page Should Be Open
    Set Username  kalle
    Set Password  kalle123
    Submit Login Credentials
    Login Should Succeed


Login After Failed Registration
    Set Username  tiina
    Set Password  tiina123
    Set Password Confirmation  maiju123
    Submit Credentials
    Register Should Fail With Message  Password and confirmation don't match
    Go To Login Page
    Login Page Should Be Open
    Set Username  tiina
    Set Password  tiina123
    Submit Login Credentials
    Login Should Fail With Message  Invalid username or password

*** Keywords ***
Register Should Succeed
    Welcome Page Should Be Open

Register Should Fail With Message
    [Arguments]  ${message}
    Register Page Should Be Open
    Page Should Contain  ${message}

Submit Credentials
    Click Button  Register

Submit Login Credentials
    Click Button  Login

Set Username
    [Arguments]  ${username}
    Input Text  username  ${username}

Set Password
    [Arguments]  ${password}
    Input Password  password  ${password}

Set Password Confirmation
    [Arguments]  ${password_confirmation}
    Input Password  password_confirmation  ${password_confirmation}

Create User And Go To Register Page
    Create User  kalle  kalle123
    Go To Register Page
    Register Page Should Be Open

Login Should Succeed
    Main Page Should Be Open

Login Should Fail With Message
    [Arguments]  ${message}
    Login Page Should Be Open
    Page Should Contain  ${message}