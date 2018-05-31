def reverse(input=''):
    i=len(input)-1
    output=""
    while i>=0:
        output+=input[i]
        i-=1
    return(output)