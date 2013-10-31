def add_numbers( number1, number2 ):
    '''
        Add numbers (ints or floats)

        @param number1 - List or single number
        @param number2 - List or single number
    '''
    n1type = type( number1 )
    n2type = type( number2 )

    # Both params are not lists but one of them is !!!
    if (n1type == list  or n2type == list) and n1type != n2type:
        raise ValueError( "Cannot specify only one list as a parameter" )

    if n1type == list:
        sums = []
        for n1, n2 in zip( number1, number2 ):
            sums.append( n1 + n2 )
        return sums
    else:
        return number1 + number2
