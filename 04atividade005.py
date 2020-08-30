def verificar(caracter):

if caracter in"aeiouAEIOU":
    return f"vogal"
elif caracter in "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ":
    return f"consoante"
elif caracter in "0123456789":
    return f"número"
else:
    return f"símbolo"

        
