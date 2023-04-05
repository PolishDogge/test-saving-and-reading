from random import randint
import ast

skip = False


def convert(mes):
    if type(mes) == list:
        return mes
    elif type(mes) == str:
        x = ast.literal_eval(mes)
    return x

def convertstr(message):
    if type(message) == str:
        return message
    else:
        return str(message)

def DEncode(message, move) -> list:
    global skip
    loop = []
    output = []
    message = convertstr(message)
    for character in message:
        loop = []
        if character.isupper(): # Check if the character is uppercase
            loop.append(int(2))
            character = character.lower() # If it is, set it to lowercase
        elif character.islower():
            loop.append(int(1))
            character = character.lower() 
        elif character.isspace(): # Check if the character is a space
            loop.append(int(0))
            loop.append(randint(-255, 255))
            output.append(loop)
            continue
        elif character.isnumeric(): # Check if the character is a number
            loop.append(int(5))
            loop.append(int(character))
            output.append(loop)
            continue # Check if the character is a special character
        elif character in [ 
            "{",
            "}",
            "[",
            "]",
            "(",
            ")",
            "<",
            ">",
            "/",
            "\\",
            "|",
            "?",
            "!",
            "@",
            "#",
            "$",
            "%",
            "^",
            "&",
            "*",
            "-",
            "_",
            "+",
            "=",
            "~",
            "`",
            "'",
            '"',
            ":",
            ";",
            ".",
            ",",
        ]:
            loop.append(int(10))
            loop.append(ord(character))
            output.append(loop)
            continue
        
        # convert character to number
        #print(f'Character = {character}')
        number = ord(character) - move

        # add random number to loop
        if int(randint(0, 1000)) >= 350:
            k = randint(0, 1000)
            number = number + k
            loop.append(k)
            loop.append(number)
            skip = True

        # add number to loop
        if skip == False:
            loop.append(number)

        # add to output
        output.append(loop)
        skip = False
    output.append(move)
    return output


def DDecode(msg) -> str:
    final = []
    which = -1
    msg = convert(msg)
    skip = False
    fulllen = len(msg)
    move = msg[fulllen - 1]  # Get the move number from the end of the message
    msg.pop(fulllen - 1)  # Remove the move number from the message

    for x in msg:
        which = 0
        for y in x:
            which = which + 1
            print(which)
            # Loop through each character in the message
            try:
                if y == x[2]:
                    continue
            except IndexError:
                pass  # If there is no 3rd character, skip (Dumb way of doing it, but it works)
            
            if y == x[0]:
                if y == 0:
                    final.append(" ")  # If the first character is 0, add a space
                    skip = True
                    continue
                
                if y == 1:
                    out = False  # If the first character is 1, set out to false (This is for non-capital letters)
                if y == 2:
                    out = True  # If the first character is 2, set out to true (This is for capital letters)
                if y == 5:
                    try:
                        final.append(
                            str(x[which])
                        )  # If the first character is 5, add the second character to the final message
                    except IndexError:
                        # f this, its so dumb, i updated it because apaprently it outputs a number 5 twice otherwise
                        pass
                    skip = True
                    continue
                
                if y == 10:
                    try:
                        final.append(
                            chr(x[which])
                        )  # If the first character is 10, add the second character to the final message   
                    except IndexError:
                        # If i did it for the 5s, might as well implement it here
                        pass
                    skip = True
                    continue
            else:
            
                try:
                    if x[2]:
                        y = (
                            x[2] - y
                        )  # If there is a third character, subtract it from the second character (This is for messing with the message)
                except IndexError:
                    pass  # Again, the 'best way'
                
                if skip:
                    skip = False  # If skip is true, set it to false and skip the rest of the loop
                    continue
                
                if out:
                    final.append(chr(y + move).upper())
                else:  # If out is false, add the character to the final message
                    final.append(chr(y + move))
        final1 = "".join(final)  # Join the final message into a string and return it
    return final1