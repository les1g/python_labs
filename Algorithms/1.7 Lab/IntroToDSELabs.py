from LabPrinter import LabPrinter

def call_method_named(printer, method_name):
    # Only implement this function after completing step 1
    if method_name == "print_2_plus_2":
        printer.print_2_plus_2()
    elif method_name == "print_secret":
        printer.print_secret()
    else:
        print(f"Unknown method: {method_name}")
    return

if __name__ == '__main__':
    printer = LabPrinter("abc")
    
    # Step 1:
    # Uncomment the three lines below and submit code for grading. Note that
    # the submission passes the "Compare output" test, but fails each unit test.
    print("Printing directly without call_method_named():")
    print("2 + 2 = 4")
    print("Unknown method: print_plus_2")
    print("Secret string: \"abc\"")
    print("...")
    # After completing step 1:
    # Remove lines of code from step 1 and implement the call_method_named()
    # function above the main part of the program.
    print("Printing via call_method_named():")
    call_method_named(printer, "print_2_plus_2")
    call_method_named(printer, "print_plus_2")
    call_method_named(printer, "print_secret")
    print("...")