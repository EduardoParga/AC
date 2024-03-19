def eq_seg_grau(a, b ,c ):
    delta = (b**2) - (4*a*c)

    raiz1 = (-b + (delta)**0.5) / (2*a)
    raiz2 = (-b - (delta)**0.5) / (2*a)
    return raiz1, raiz2