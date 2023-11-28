from classvector import vector2D
from classvector import vector3D



vec2d = vector2D(3,8)
vec2d2 = vector2D(5,6)
vec3d = vector3D(3,5,9)
vec3d2 = vector3D(3,5,9)


vec2d.TOSTRING()
vec2d.norm()
if vec2d.equals(vec2d2)==True:
    print("the coordinates of the two vector are equals.")
else:
    print("the coordinates of the two vector are not equals.")


vec3d.TOSTRING()
vec3d.norm()
if vec3d.equals(vec3d2)==True:
    print("the coordinates of the two vector are equals.")
else:
    print("the coordinates of the two vector are not equals.")