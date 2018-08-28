while True: # try forever, potentially
    try: # anything that might throw an exception goes in here
        x = int(input("Please enter a number: "))
        # if a ValueError exception happens in the above line,
        # we DO NOT CONTINUE this try block,
        # and we immediately go to the except block
        
        break # get out of the loop once the user does the right thing
    except ValueError:
        # in here, we deal with any exceptions thrown
        # we only got here if a ValueError happened
        # in this case, we say we only know how to deal with ValueErrors
        print("Oops!  That was no valid number. Try again!")
