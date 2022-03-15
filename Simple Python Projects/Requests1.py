import requests
def request():
    print("Following program will give you some information about your entered API link")
    user_input = input("Enter a API : ")
    res = requests.get(user_input)
    user_request = eval(input("What do you want to know \n"
                              "(1) Enter for status code \n"
                              "(2) Enter for Text \n"
                              "(3) Enter for Cookies \n"
                              "(4) Enter for Header : "))
    if user_request == 1:
        print(res.status_code)
    elif user_request == 2:
        print(res.text)
    elif user_request == 3:
        print(res.cookies)
    elif user_request == 4:
        print(res.headers)
    again()
def again():
    user_input = eval(input("Do You Want to get more information about your API \n"
                            "(1) Enter for Yes \n"
                            "(2) Enter for No : "))
    if user_input == 1:
        print("Running program again ...")
        request()
    else:
        print("Thank You")
request()