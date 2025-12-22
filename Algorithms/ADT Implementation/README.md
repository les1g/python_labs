- **Goal of lab:**

    Learn that labs test both **output** and **implementation via ADTs/objects**.
    
- **Key function:**
    
    `call_method_named(printer, method_name)`
    
- **Behavior:**

    - `"print_2_plus_2"` → `printer.print_2_plus_2()`

    - `"print_secret"` → `printer.print_secret()`

    - anything else → `print("Unknown method: " + method_name)`

- **Grading logic:**

    - 1/10: Output correct, but you didn’t use the LabPrinter object correctly.
    
    - 10/10: Same output, but you use the **object methods**, and the hidden tests verify this.