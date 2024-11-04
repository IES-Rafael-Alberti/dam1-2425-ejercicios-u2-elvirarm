from src.condicionales.ej21_07 import asignar_tipo_impositivo

def test_asignar_tipo_impositivo():
    assert asignar_tipo_impositivo(800) == "5%"