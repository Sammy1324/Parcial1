from Point import Point
from Rectangle import Rectangle

A = Point(2, 3)
B = Point(5, 5)
C = Point(-3, -1)
D = Point(0, 0)

def show_points():

    print("Puntos:")
    print(f"A: {A}")
    print(f"B: {B}")
    print(f"C: {C}")
    print(f"D: {D}")

def show_quadrants(A=A, C=C, D=D):
    print("\nCuadrantes:")
    print(f"A pertenece al cuadrante: {A.quadrant()}")
    print(f"C pertenece al cuadrante: {C.quadrant()}")
    print(f"D pertenece al cuadrante: {D.quadrant()}")

def show_vectors(A=A, B=B):
    print("\nVectores:")
    print(f"Vector AB: {A.vector(B)}")
    print(f"Vector BA: {B.vector(A)}")

def show_distances(A=A, B=B, C=C, D=D):
    print("\nDistancias:")
    print(f"Distancia entre A y B: {A.distance(B)}")
    print(f"Distancia entre B y A: {B.distance(A)}")

    distance_A = A.distance(D)
    distance_B = B.distance(D)
    distance_C = C.distance(D)

    farther = max(distance_A, distance_B, distance_C)
    if farther == distance_A:
        print("\nEl punto más lejos del origen es A.")
    elif farther == distance_B:
        print("\nEl punto más lejos del origen es B.")
    else:
        print("\nEl punto más lejos del origen es C.")

def show_rectangle(A=A, B=B):
    rectangle = Rectangle(A, B)

    print("\nRectángulo:")
    print(f"Base: {rectangle.basis()}")
    print(f"Altura: {rectangle.height()}")
    print(f"Área: {rectangle.area()}")

def main():
    show_points()
    show_quadrants(A, C, D)
    show_vectors(A, B)
    show_distances(A, B, C, D)
    show_rectangle(A, B)