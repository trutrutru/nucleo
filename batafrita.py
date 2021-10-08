#EXECUTE
## Select the object
#bpy.data.objects['Camera'].select = True    # Blender 2.7x

## https://wiki.blender.org/wiki/Reference/Release_Notes/2.80/Python_API/Scene_and_Object_API
#bpy.data.objects['Camera'].select_set(True) # Blender 2.8x

## Select the object
#bpy.data.objects['Camera'].select = True    # Blender 2.7x

## https://wiki.blender.org/wiki/Reference/Release_Notes/2.80/Python_API/Scene_and_Object_API
#bpy.data.objects['Camera'].select_set(True) # Blender 2.8x

######3334ww;;ssggeeddfhhjj
################aaassaaasss
###lll
##ddff
# import bpy
###aaaaaaaa####yyyyyyyyy##############################333# bpy.data.objects["Cube.001"].data.vertices[1].co.y += -17.0
import bpy
from random import randint,random

# bpy.ops.collection.create(name="CubeXGroup")


###
#
#
#
# bpy.ops.object.select_all(action='SELECT')
# seleciona tudo
#

# Delete all antes de tudo

# bpy.ops.object.delete()
# bpy.ops.object.delete()

#
#


# bpy.ops.object.select_all(action='SELECT')
#
# bpy.ops.object.delete()
#
# scene = bpy.context.scene
# scene.render.image_settings.file_format = 'PNG'
# scene.render.filepath = "/home/comprimido/Desktop/bomx234234234234"
# bpy.ops.render.render(write_still = 1)







#
# #group = bpy.data.collection['CubeXGroup']
#
def main():
    start_pos=(0,0,0)
    for i in range(7):
        add_box(i);

def add_box(i):
    #generate our object
    bpy.ops.mesh.primitive_cube_add(location = [ randint(-15,15) for axis in 'xyz'])
    #Select the active object (last added is always the active one
    obj = bpy.context.active_object
    object_random_location_animation(obj,-150,150)
    object_random_color(obj,i)
    obj.select_set(state = True)
    bpy.data.collections["CubeXGroup"].objects.link(obj)

#End AddBoxin():
    start_pos=(0,0,0)
    for i in range(127):
        add_box(i);
##
def add_box(i):
    #generate our object
    bpy.ops.mesh.primitive_cube_add(location = [ randint(-15,15) for axis in 'xyz'])
    #Select the active object (last added is always the active one
    obj = bpy.context.active_object
    object_random_location_animation(obj,-15,15)
    object_random_color(obj,i)
    obj.select_set(state = True)
    bpy.data.collections["CubeXGroup"].objects.link(obj)

#End AddBox

def object_random_location_animation(obj,min,max):
    positions =  []
    for i in range(0,9):
        positions.append([ randint(min,max) for axis in 'xyz'])

    frame_num = 0
    for position in positions:
        bpy.context.scene.frame_set(frame_num)
        obj.location = position
        obj.keyframe_insert(data_path="location",index = -1)
        frame_num +=30
#End object_random_location_animation

def  object_random_color(obj,i):
    material = bpy.data.materials.new(name = "RandomMaterial" + str(i))
    obj.data.materials.append(material)
    bpy.context.object.active_material.diffuse_color = (random(),random(), random(),1)
   # bpy.context.object.active_material.name = "Object Material"
    #inputs[0].default_value = (random(),random(), random(), 1)
    #NOTE: Colours may be very interesting or not so great
    #You can select colours from a list of predefined colours
#End  object_random_color

main();
