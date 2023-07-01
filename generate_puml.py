# import py2puml
# import sys
# #from rigid_body import RigidBody
# from rigid_bodies_uml.rigid_body_uml import RigidBody
#
# # if __name__ == '__main__':
# #     generator = py2puml
# generator = py2puml.Generator()
# rigid = RigidBody()
#
# # Add your classes or functions to the generator
# generator.add(rigid)
#
# # Generate the PlantUML code
# plantuml_code = generator.generate()
#
# # Output the PlantUML code
# print(plantuml_code)

from py2puml.py2puml import py2puml

# outputs the PlantUML content in the terminal
print(''.join(py2puml('rigid_bodies_uml', 'rigid_bodies_uml')))

# writes the PlantUML content in a file
with open('rigid_bodies_uml/domain.puml', 'w') as puml_file:
    puml_file.writelines(py2puml('rigid_bodies_uml', 'rigid_bodies_uml'))