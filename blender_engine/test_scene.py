import bpy
import os

# Clear existing objects
bpy.ops.object.select_all(action='SELECT')
bpy.ops.object.delete(use_global=False)

# Remove default cube if exists
if "Cube" in bpy.data.objects:
    bpy.data.objects.remove(bpy.data.objects["Cube"], do_unlink=True)

# Create a cube
bpy.ops.mesh.primitive_cube_add(size=2, location=(0, 0, 1))
cube = bpy.context.active_object
cube.name = "TestCube"

# Add a metal material
metal_mat = bpy.data.materials.new(name="MetalMaterial")
metal_mat.use_nodes = True
nodes = metal_mat.node_tree.nodes
principled_bsdf = nodes.get("Principled BSDF")
if principled_bsdf:
    principled_bsdf.inputs["Base Color"].default_value = (0.8, 0.8, 0.8, 1.0)
    principled_bsdf.inputs["Metallic"].default_value = 1.0
    principled_bsdf.inputs["Roughness"].default_value = 0.2

if cube.data.materials:
    cube.data.materials[0] = metal_mat
else:
    cube.data.materials.append(metal_mat)

# Add a ground plane
bpy.ops.mesh.primitive_plane_add(size=10, location=(0, 0, 0))
plane = bpy.context.active_object
plane.name = "GroundPlane"

# Add material to ground
ground_mat = bpy.data.materials.new(name="GroundMaterial")
ground_mat.use_nodes = True
nodes = ground_mat.node_tree.nodes
principled_bsdf = nodes.get("Principled BSDF")
if principled_bsdf:
    principled_bsdf.inputs["Base Color"].default_value = (0.2, 0.2, 0.2, 1.0)
    principled_bsdf.inputs["Roughness"].default_value = 0.8

if plane.data.materials:
    plane.data.materials[0] = ground_mat
else:
    plane.data.materials.append(ground_mat)

# Set up two area lights
# Light 1
bpy.ops.object.light_add(type='AREA', location=(3, -3, 4))
light1 = bpy.context.active_object
light1.name = "AreaLight1"
light1.data.energy = 500
light1.data.size = 2
light1.data.color = (1.0, 0.9, 0.8)
light1.rotation_euler = (0.5, 0, 0.785)

# Light 2
bpy.ops.object.light_add(type='AREA', location=(-3, -3, 4))
light2 = bpy.context.active_object
light2.name = "AreaLight2"
light2.data.energy = 300
light2.data.size = 2
light2.data.color = (0.8, 0.9, 1.0)
light2.rotation_euler = (0.5, 0, 2.356)

# Add a camera
bpy.ops.object.camera_add(location=(5, -5, 5))
camera = bpy.context.active_object
camera.name = "TestCamera"
camera.rotation_euler = (0.7, 0, 0.785)

# Set as active camera
bpy.context.scene.camera = camera

# Configure render settings
bpy.context.scene.render.engine = 'CYCLES'
bpy.context.scene.cycles.samples = 128
bpy.context.scene.render.resolution_x = 1920
bpy.context.scene.render.resolution_y = 1080

# Ensure output directory exists
output_dir = "/tmp/blender_render"
os.makedirs(output_dir, exist_ok=True)

# Set output path
bpy.context.scene.render.filepath = os.path.join(output_dir, "test_scene.png")

# Render the scene
bpy.ops.render.render(write_still=True)

print("Scene created and rendered successfully!")
print(f"Output saved to: {bpy.context.scene.render.filepath}")
