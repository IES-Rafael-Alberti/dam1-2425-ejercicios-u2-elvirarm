from src.condicionales.ej21_02 import mostrar_contrasenia

def test_mostrar_contrasenia():
    assert mostrar_contrasenia("contraseña", "contraseña") == "contraseña"