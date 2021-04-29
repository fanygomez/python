from setuptools import setup

setup(
    name= "paquetecalculos",
    version="1.0",description="Paquete de calculos basicos y avanzados",
    author="Stefhani",
    author_email="go.maryory@gmail.com",
    url="www",
    #Agregar los paquetes que desean empaquetar
    packages=["calculos","calculos.redondeo_potencia"]
)