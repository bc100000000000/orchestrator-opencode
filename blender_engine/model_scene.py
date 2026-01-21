import bpy
import random
import math

# Clear existing objects
bpy.ops.object.select_all(action='SELECT')
bpy.ops.object.delete(use_global=False)

# Remove existing materials
for material in bpy.data.materials:
    bpy.data.materials.remove(material)

# ============================================
# MATERIALS
# ============================================

# Dark metallic floor material
def create_dark_metal_material():
    mat = bpy.data.materials.new(name="DarkMetal")
    mat.use_nodes = True
    nodes = mat.node_tree.nodes
    links = mat.node_tree.links
    
    nodes.clear()
    
    output = nodes.new(type='ShaderNodeOutputMaterial')
    principled = nodes.new(type='ShaderNodeBsdfPrincipled')
    
    principled.inputs['Base Color'].default_value = (0.02, 0.02, 0.03, 1)
    principled.inputs['Metallic'].default_value = 0.9
    principled.inputs['Roughness'].default_value = 0.3
    principled.inputs['Specular IOR Level'].default_value = 0.5
    
    links.new(principled.outputs['BSDF'], output.inputs['Surface'])
    
    return mat

# Glowing cyan ring material
def create_cyan_glow_material():
    mat = bpy.data.materials.new(name="CyanGlow")
    mat.use_nodes = True
    nodes = mat.node_tree.nodes
    links = mat.node_tree.links
    
    nodes.clear()
    
    output = nodes.new(type='ShaderNodeOutputMaterial')
    principled = nodes.new(type='ShaderNodeBsdfPrincipled')
    emission = nodes.new(type='ShaderNodeEmission')
    mix_shader = nodes.new(type='ShaderNodeMixShader')
    
    principled.inputs['Base Color'].default_value = (0.0, 0.1, 0.15, 1)
    principled.inputs['Metallic'].default_value = 0.8
    principled.inputs['Roughness'].default_value = 0.2
    principled.inputs['Emission Color'].default_value = (0.0, 1.0, 1.0, 1)
    principled.inputs['Emission Strength'].default_value = 5.0
    
    mix_shader.inputs[0].default_value = 0.3
    links.new(principled.outputs['BSDF'], mix_shader.inputs[1])
    links.new(emission.outputs['Emission'], mix_shader.inputs[2])
    links.new(mix_shader.outputs['Shader'], output.inputs['Surface'])
    
    return mat

# Column material
def create_column_material():
    mat = bpy.data.materials.new(name="ColumnMaterial")
    mat.use_nodes = True
    nodes = mat.node_tree.nodes
    links = mat.node_tree.links
    
    nodes.clear()
    
    output = nodes.new(type='ShaderNodeOutputMaterial')
    principled = nodes.new(type='ShaderNodeBsdfPrincipled')
    
    principled.inputs['Base Color'].default_value = (0.1, 0.1, 0.12, 1)
    principled.inputs['Metallic'].default_value = 0.95
    principled.inputs['Roughness'].default_value = 0.15
    principled.inputs['Specular IOR Level'].default_value = 0.8
    
    links.new(principled.outputs['BSDF'], output.inputs['Surface'])
    
    return mat

# Holographic disk material with random colors
def create_holo_material(color):
    mat = bpy.data.materials.new(name=f"Holochrome_{color[0]:.0f}_{color[1]:.0f}_{color[2]:.0f}")
    mat.use_nodes = True
    mat.blend_method = 'BLEND'
    nodes = mat.node_tree.nodes
    links = mat.node_tree.links
    
    nodes.clear()
    
    output = nodes.new(type='ShaderNodeOutputMaterial')
    principled = nodes.new(type='ShaderNodeBsdfPrincipled')
    transparent = nodes.new(type='ShaderNodeBsdfTransparent')
    mix_shader = nodes.new(type='ShaderNodeMixShader')
    
    principled.inputs['Base Color'].default_value = color
    principled.inputs['Alpha'].default_value = 0.6
    principled.inputs['Emission Color'].default_value = color
    principled.inputs['Emission Strength'].default_value = 3.0
    principled.inputs['Roughness'].default_value = 0.0
    principled.inputs['Metallic'].default_value = 0.0
    
    mix_shader.inputs[0].default_value = 0.5
    links.new(principled.outputs['BSDF'], mix_shader.inputs[1])
    links.new(transparent.outputs['BSDF'], mix_shader.inputs[2])
    links.new(mix_shader.outputs['Shader'], output.inputs['Surface'])
    
    return mat

# ============================================
# SCENE CREATION
# ============================================

# Floor
bpy.ops.mesh.primitive_plane_add(size=30, location=(0, 0, 0))
floor = bpy.context.active_object
floor.name = "Floor"
floor.data.materials.append(create_dark_metal_material())

# Central platform
bpy.ops.mesh.primitive_cylinder_add(radius=3, depth=0.3, location=(0, 0, 0.15))
platform = bpy.context.active_object
platform.name = "CentralPlatform"
platform.data.materials.append(create_dark_metal_material())

# Glowing cyan ring on platform
bpy.ops.mesh.primitive_torus_add(
    major_radius=2.5,
    minor_radius=0.1,
    location=(0, 0, 0.31)
)
ring = bpy.context.active_object
ring.name = "CyanRing"
ring.data.materials.append(create_cyan_glow_material())

# Decorative columns (8 around the scene)
column_material = create_column_material()
column_positions = []

for i in range(8):
    angle = (i / 8) * 2 * math.pi
    x = math.cos(angle) * 8
    y = math.sin(angle) * 8
    
    # Column base
    bpy.ops.mesh.primitive_cylinder_add(radius=0.4, depth=0.3, location=(x, y, 0.15))
    base = bpy.context.active_object
    base.name = f"ColumnBase_{i}"
    base.data.materials.append(column_material)
    
    # Column shaft
    bpy.ops.mesh.primitive_cylinder_add(radius=0.25, depth=4, location=(x, y, 2.15))
    shaft = bpy.context.active_object
    shaft.name = f"ColumnShaft_{i}"
    shaft.data.materials.append(column_material)
    
    # Column capital
    bpy.ops.mesh.primitive_cylinder_add(radius=0.5, depth=0.4, location=(x, y, 4.25))
    capital = bpy.context.active_object
    capital.name = f"ColumnCapital_{i}"
    capital.data.materials.append(column_material)
    
    column_positions.append((x, y))

# Floating holographic disks
disk_colors = [
    (1.0, 0.2, 0.3, 1),  # Red
    (0.2, 1.0, 0.4, 1),  # Green
    (1.0, 0.8, 0.2, 1),  # Yellow
    (0.8, 0.2, 1.0, 1),  # Purple
    (0.2, 0.8, 1.0, 1),  # Blue
]

for i in range(5):
    x = random.uniform(-6, 6)
    y = random.uniform(-6, 6)
    z = random.uniform(2, 5)
    
    bpy.ops.mesh.primitive_cylinder_add(radius=random.uniform(0.3, 0.8), depth=0.05, location=(x, y, z))
    disk = bpy.context.active_object
    disk.rotation_euler = (math.radians(90), 0, 0)
    disk.name = f"HoloDisk_{i}"
    
    color = random.choice(disk_colors)
    disk.data.materials.append(create_holo_material(color))

# ============================================
# LIGHTING - Three-point setup
# ============================================

# Warm key light
bpy.ops.object.light_add(type='SPOT', location=(8, -8, 10))
key_light = bpy.context.active_object
key_light.name = "KeyLight"
key_light.data.energy = 3000
key_light.data.color = (1.0, 0.9, 0.7)
key_light.data.spot_size = math.radians(60)
key_light.rotation_euler = (math.radians(45), 0, math.radians(45))

# Cool fill light
bpy.ops.object.light_add(type='AREA', location=(-6, 6, 3))
fill_light = bpy.context.active_object
fill_light.name = "FillLight"
fill_light.data.energy = 800
fill_light.data.color = (0.3, 0.4, 0.8)
fill_light.data.size = 5
fill_light.rotation_euler = (math.radians(30), 0, math.radians(-135))

# Cyan rim light
bpy.ops.object.light_add(type='SPOT', location=(0, 0, 8))
rim_light = bpy.context.active_object
rim_light.name = "RimLight"
rim_light.data.energy = 2000
rim_light.data.color = (0.0, 1.0, 1.0)
rim_light.data.spot_size = math.radians(90)
rim_light.rotation_euler = (math.radians(90), 0, 0)

# ============================================
# CAMERA
# ============================================

# Camera
bpy.ops.object.camera_add(location=(12, -12, 8))
camera = bpy.context.active_object
camera.name = "MainCamera"
camera.rotation_euler = (math.radians(60), 0, math.radians(45))

# Tracking target
bpy.ops.object.empty_add(type='PLAIN_AXES', location=(0, 0, 2))
target = bpy.context.active_object
target.name = "CameraTarget"

# Add tracking constraint to camera
track_constraint = camera.constraints.new(type='TRACK_TO')
track_constraint.target = target
track_constraint.track_axis = 'TRACK_NEGATIVE_Z'
track_constraint.up_axis = 'UP_Y'

# Set as active camera
bpy.context.scene.camera = camera

# ============================================
# WORLD / ENVIRONMENT
# ============================================

world = bpy.context.scene.world
if world is None:
    world = bpy.data.worlds.new("World")
    bpy.context.scene.world = world

world.use_nodes = True
nodes = world.node_tree.nodes
links = world.node_tree.links

nodes.clear()

background = nodes.new(type='ShaderNodeBackground')
background.inputs['Color'].default_value = (0.01, 0.01, 0.02, 1)
background.inputs['Strength'].default_value = 0.5

output = nodes.new(type='ShaderNodeOutputWorld')
links.new(background.outputs['Background'], output.inputs['Surface'])

# ============================================
# RENDER SETTINGS
# ============================================

bpy.context.scene.render.engine = 'CYCLES'
bpy.context.scene.cycles.samples = 128
bpy.context.scene.render.resolution_x = 1920
bpy.context.scene.render.resolution_y = 1080
bpy.context.scene.render.filepath = "/tmp/blender_render/scifi_room.png"

# Ensure output directory exists
import os
os.makedirs("/tmp/blender_render", exist_ok=True)

# Render
bpy.ops.render.render(write_still=True)

print("Sci-fi scene rendered successfully!")
