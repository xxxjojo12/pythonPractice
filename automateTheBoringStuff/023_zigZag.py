import time, sys

indent = 0  # How many spaces to indent.
indentIncreasing = True # Whether the indentation is increasing or not.

try:
    while True:
        print(' ' * indent, end='')
        print('********')
        time.sleep(0.03) # Pause for 1/10 of a second.

        if indentIncreasing:
            indent += 1
            if indent == 40:
                indentIncreasing = False
        
        else:
            indent -= 1
            if indent == 0:
                indentIncreasing = True

except KeyboardInterrupt:
    sys.exit()