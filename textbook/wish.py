program_status = True
message = ""
countries = []
user_res = "Enter a list of countries you'd like to visit in 2021... \nenter quit to end program: "

while program_status:
    message = input(user_res)

    if message.lower() == "quit":
        program_status = False
        print(f"Here is a list of your countries below: \n {countries}")
        break

    countries.append(message)