from django.core.exceptions import ValidationError

def validar_cadena_simple(cadena: str, minimo: int, maximo: int):
    if not cadena.isalpha():
        raise ValidationError("Este campo solo puede contener letras")
    
    if len(cadena) < minimo or len(cadena) > maximo:
        raise ValidationError(f"Este campo debe tener una longitud de entre {minimo} y {maximo} caracteres")
        
def validar_dni(dni: str):
    if not dni.isdigit():
         raise ValidationError("Este campo solo puede contener caracteres numericos")
    
    if len(dni) < 8:
         raise ValidationError("Este campo debe tener una longitud de 8 digitos")
    
def validar_cadena_compuesta(cadena: str, minimo: int, maximo: int):
    if len(cadena) < minimo or len(cadena) > maximo:
        raise ValidationError(f"Este campo debe tener una longitud de entre {minimo} y {maximo} caracteres")
    
