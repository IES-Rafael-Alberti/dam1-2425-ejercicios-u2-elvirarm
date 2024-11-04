from src.condicionales.ej21_05 import comprobar_tributacion
def test_comprobar_tributacion():
    assert comprobar_tributacion(10,400) == "No puedes tributar."