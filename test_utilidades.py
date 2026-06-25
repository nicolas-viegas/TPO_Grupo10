from parking.utilidades import validar_patente, cadena_a_entero, division_segura

# 1. Caso de prueba: Validación de patentes (Regex)
def test_validar_patente():
    # Casos válidos
    assert validar_patente("AB123CD") == True
    assert validar_patente("ABC123") == True
    assert validar_patente("ab123cd") == True  # Debe aceptar minúsculas y normalizar
    assert validar_patente(" abc123 ") == True # Debe ignorar espacios al inicio/fin
    
    # Casos inválidos
    assert validar_patente("A123BCD") == False # Formato mezclado
    assert validar_patente("1234567") == False # Solo números
    assert validar_patente("") == False        # Vacío

# 2. Caso de prueba: Conversión de cadenas a enteros
def test_cadena_a_entero():
    # Casos válidos
    assert cadena_a_entero("15") == 15
    assert cadena_a_entero("  8  ") == 8 # Debe limpiar espacios
    assert cadena_a_entero("0") == 0
    
    # Casos inválidos (deben devolver None según la lógica de tu función)
    assert cadena_a_entero("-5") is None       # No se permiten números negativos
    assert cadena_a_entero("letras") is None   # No es numérico
    assert cadena_a_entero("") is None         # Vacío
    assert cadena_a_entero(None) is None       # Tipo nulo

# 3. Caso de prueba: División segura
def test_division_segura():
    # División normal
    assert division_segura(10, 2) == 5.0
    assert division_segura(9, 3) == 3.0
    
    # División por cero (debe atajarlo y devolver None)
    assert division_segura(10, 0) is None