def format(number,fmt):
    '''
        'o'-octal
        'b'-binary
        'x'-hexadecimal
    '''

    if fmt == 'o':
        result = "{:o}".format(number)
    elif fmt == 'b':
        result = "{:b}".format(number)
    elif fmt =='x':
        result = "{:x}".format(number)
    
    else:
        result = str(number)
    return result

formatted_result = format(145,'o')
print("Formatted Result :", formatted_result)