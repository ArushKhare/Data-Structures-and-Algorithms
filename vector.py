"""Vector Functions"""

import math

class GeoVector:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
    
    def __eq__(self, other):
        return (self.x == other.x) and (self.y == other.y) and (self.z == other.z)
    
    def __repr__(self):
        return str((self.x, self.y, self.z))
    
    def magnitude(self):
        return math.sqrt(self.x**2 + self.y**2 + self.z**2)
    
    def scalar_multiply(self, scalar):
        self.x *= scalar
        self.y *= scalar
        self.z *= scalar
        return (self.x, self.y, self.z)


def addition(vectorA: GeoVector, vectorB: GeoVector):
    return GeoVector(vectorA.x + vectorB.x, vectorA.y + vectorB.y, vectorA.z + vectorB.z)

def subtraction(vectorA: GeoVector, vectorB: GeoVector):
    return GeoVector(vectorA.x - vectorB.x, vectorA.y - vectorB.y, vectorA.z - vectorB.z)

def dot_product(vectorA: GeoVector, vectorB: GeoVector):
    return (vectorA.x * vectorB.x) + (vectorA.y * vectorB.y) + (vectorA.z * vectorB.z)

def cross_product(vectorA: GeoVector, vectorB: GeoVector):
    return GeoVector(vectorA.y*vectorB.z-vectorA.z*vectorB.y, 
                     vectorA.z*vectorB.x-vectorA.x*vectorB.z, 
                     vectorA.x*vectorB.y-vectorA.y*vectorB.x)

def projection(vector: GeoVector, direction_vector: GeoVector):
    multiplier = dot_product(vector, direction_vector) / (direction_vector.magnitude()**2)
    return GeoVector(multiplier*direction_vector.x, 
                     multiplier*direction_vector.y, 
                     multiplier*direction_vector.z)

def projection_magnitude(vector: GeoVector, direction_vector: GeoVector):
    assert vector and direction_vector
    return abs(dot_product(vector, direction_vector))/direction_vector.magnitude()

def linear_transform(vector: GeoVector, matrix: list):
    assert len(matrix[0]) == 3
    new_x = dot_product(GeoVector(matrix[0][0], matrix[0][1], matrix[0][2]), vector)
    new_y = dot_product(GeoVector(matrix[1][0], matrix[1][1], matrix[1][2]), vector)
    new_z = dot_product(GeoVector(matrix[2][0], matrix[2][1], matrix[2][2]), vector)
    return GeoVector(new_x, new_y, new_z)

def angle(vectorA: GeoVector, vectorB: GeoVector):
    return math.acos(dot_product(vectorA, vectorB)/(vectorA.magnitude()*vectorB.magnitude()))

def angle_type(vectorA: GeoVector, vectorB: GeoVector):
    dot_product_value = dot_product(vectorA, vectorB)
    if dot_product_value < 0:
        # Obtuse angle between vectors
        return -1
    if dot_product_value == 0:
        # Orthogonal vectors
        return 0
    if dot_product_value > 1:
        # Acute angle between vectors
        return 1
    

if __name__ == '__main__':
    # Initialize vectors v1 and v2
    v1 = GeoVector(1, -1, -5)
    v2 = GeoVector(1, 5, 9)
    print(f"v1={v1}, v2={v2}\n")

    # Angle between v1 and v2 (in radians)
    print("Angle between v1 and v2:", angle(v1, v2),'\n')

    # Angle type of angle between v1 and v2 {-1: obtuse, 0: right, 1: acute}
    print("Type of angle between v1 and v2:", angle_type(v1, v2),'\n')

    # Projection of v1 on v2
    print("Projection of v1 on v2:", projection(v1, v2),'\n')

    # Magnitude of projection of v1 on v2
    print("Magnitude of projection of v1 on v2:", projection_magnitude(v1, v2),'\n')

    # Cross Product of v1 and v2
    print("Cross product of v1 and v2:", cross_product(v1, v2),'\n')

    # Dot Product of v1 and v2
    print("Dot product of v1 and v2:", dot_product(v1, v2),'\n')

    # Addition of v1 and v2
    print("Result of v1+v2:", addition(v1, v2),'\n')

    # Subtraction of v1 and v2
    print("Result of v1-v2:", subtraction(v1, v2),'\n')

    # Linear transformation of v1 using matrix [1 2 -1; 1 4 5; -1 0 1]
    transformation_matrix = [[1, 2, -1], [1, 4, 5], [-1, 0, 1]]
    print("Transformed vector v1:", linear_transform(v1, transformation_matrix),'\n')

    # Linear transformation of v2 using identity matrix [1 0 0; 0 1 0; 0 0 1] (vector shouldn't change)
    identity_matrix = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
    transformed_v2 = linear_transform(v2, identity_matrix)
    print("Transformed vector v2:", transformed_v2,'\n')
    print("Is transformed_v2 equal to v2?:", transformed_v2 == v2,'\n')
