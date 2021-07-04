def compruebaMail(mailUsuario):
    """
    -----------------------------------------------------------------
    Pruebas dentro de la documentacion usando el modulo doctest
    -----------------------------------------------------------------
    La función compruebaMail evalúa un mail recibido en busca de la @.
        Si tiene una @ es correcto, si tiene más de una @ es incorrecto
        si la @ está al final es incorrecto.
    >>> compruebaMail('fanygomez@gmail.com')
    True
    >>> compruebaMail('fanygomez.com')
    False

    >>> compruebaMail('fanyg@mez@gmail.com')
    False
    """
    arroba = mailUsuario.count('@')
    if (arroba != 1 or mailUsuario.rfind('@') == (len(mailUsuario), -1) or mailUsuario.find('@') == 0):
        return False
    else:
        return True


import doctest
doctest.testmod()
