from Punto import Punto
from Rectangulo import Rectangulo

A = Punto(2, 3)
B = Punto(5, 5)
C = Punto(-3, -1)
D = Punto(0, 0)

def mostrar_puntos():

    print("Puntos:")
    print(f"A: {A}")
    print(f"B: {B}")
    print(f"C: {C}")
    print(f"D: {D}")

def mostrar_cuadrantes(A=A, C=C, D=D):
    print("\nCuadrantes:")
    print(f"A pertenece al cuadrante: {A.cuadrante()}")
    print(f"C pertenece al cuadrante: {C.cuadrante()}")
    print(f"D pertenece al cuadrante: {D.cuadrante()}")

def mostrar_vectores(A=A, B=B):
    print("\nVectores:")
    print(f"Vector AB: {A.vector(B)}")
    print(f"Vector BA: {B.vector(A)}")

def mostrar_distancias(A=A, B=B, C=C, D=D):
    print("\nDistancias:")
    print(f"Distancia entre A y B: {A.distancia(B)}")
    print(f"Distancia entre B y A: {B.distancia(A)}")

    distancia_A = A.distancia(D)
    distancia_B = B.distancia(D)
    distancia_C = C.distancia(D)

    mas_lejos = max(distancia_A, distancia_B, distancia_C)
    if mas_lejos == distancia_A:
        print("\nEl punto más lejos del origen es A.")
    elif mas_lejos == distancia_B:
        print("\nEl punto más lejos del origen es B.")
    else:
        print("\nEl punto más lejos del origen es C.")

def mostrar_rectangulo(A=A, B=B):
    rectangulo = Rectangulo(A, B)

    print("\nRectángulo:")
    print(f"Base: {rectangulo.base()}")
    print(f"Altura: {rectangulo.altura()}")
    print(f"Área: {rectangulo.area()}")

def main():
    mostrar_puntos()
    mostrar_cuadrantes(A, C, D)
    mostrar_vectores(A, B)
    mostrar_distancias(A, B, C, D)
    mostrar_rectangulo(A, B)