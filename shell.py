import basic

keep_going = True
while keep_going:
    text = input('Typical ::> ')
    if "quit" in text.lower() or "exit" in text.lower(): keep_going = False
    result, error = basic.run('<stdin>', text)

    if error: print(error.as_string())
    else: print(result)