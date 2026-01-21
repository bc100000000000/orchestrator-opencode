#!/usr/bin/env python3
"""
Blender CLI Tool
A comprehensive command-line interface for Blender operations.
Supports interactive mode, script execution, and Python integration.
"""

import argparse
import sys
import os
import subprocess
from pathlib import Path


class BlenderTool:
    """Blender CLI Tool for managing Blender operations."""
    
    def __init__(self):
        self.blender_executable = self._find_blender()
    
    def _find_blender(self) -> str:
        """Find Blender executable in system PATH."""
        blender_names = ['blender', 'blender3.6', 'blender3.7', 'blender3.8', 'blender4.0', 'blender4.1']
        
        for name in blender_names:
            try:
                result = subprocess.run(
                    ['which', name],
                    capture_output=True,
                    text=True,
                    timeout=5
                )
                if result.returncode == 0:
                    return name
            except (subprocess.TimeoutExpired, FileNotFoundError):
                continue
        
        return 'blender'  # Default to 'blender' if not found
    
    def _get_blender_args(self, python_code: str = None, python_file: str = None) -> list:
        """Get Blender command arguments."""
        args = [self.blender_executable, '--background']
        
        if python_code:
            args.extend(['--python-expr', python_code])
        elif python_file:
            args.extend(['--python', python_file])
        
        return args
    
    def build(self, scene_type: str = 'default', interactive: bool = False):
        """Build a new Blender scene."""
        python_code = f"""
import bpy
import random

# Clear existing objects
bpy.ops.object.select_all(action='SELECT')
bpy.ops.object.delete(use_global=False)

# Remove default collections content
for collection in bpy.data.collections:
    for obj in collection.objects:
        bpy.data.objects.remove(obj)

# Create scene based on type
if '{scene_type}' == 'default':
    # Create a simple scene
    bpy.ops.mesh.primitive_cube_add(size=2, location=(0, 0, 1))
    bpy.ops.mesh.primitive_plane_add(size=10, location=(0, 0, 0))
    
elif '{scene_type}' == 'architectural':
    # Create architectural scene
    bpy.ops.mesh.primitive_cube_add(size=3, location=(0, 0, 1.5))
    bpy.ops.mesh.primitive_plane_add(size=20, location=(0, 0, 0))
    bpy.ops.mesh.primitive_cube_add(size=1, location=(2, 2, 0.5))
    
elif '{scene_type}' == 'character':
    # Create character scene (simplified)
    bpy.ops.mesh.primitive_uv_sphere_add(radius=1, location=(0, 0, 2))
    bpy.ops.mesh.primitive_cylinder_add(radius=0.3, depth=1.5, location=(0, 0, 0.8))
    bpy.ops.mesh.primitive_cone_add(radius1=0.8, depth=0.8, location=(0, 0, 3))
    
else:
    # Default fallback
    bpy.ops.mesh.primitive_cube_add(size=1, location=(0, 0, 0.5))
    bpy.ops.mesh.primitive_plane_add(size=5, location=(0, 0, 0))

print("Scene built successfully with type: '{scene_type}'")
"""
        
        args = self._get_blender_args(python_code=python_code)
        self._run_blender(args)
    
    def material(self, material_type: str = ' principled', name: str = 'NewMaterial', interactive: bool = False):
        """Create or modify materials."""
        python_code = f"""
import bpy
import random

# Create material
mat = bpy.data.materials.new(name='{name}')
mat.use_nodes = True

# Get nodes
nodes = mat.node_tree.nodes
links = mat.node_tree.links

# Clear default nodes
nodes.clear()

# Create output node
output = nodes.new('ShaderNodeOutputMaterial')
output.location = (400, 0)

# Create material based on type
if '{material_type}' == 'principled':
    # PBR Material
    principled = nodes.new('ShaderNodeBsdfPrincipled')
    principled.location = (0, 0)
    links.new(principled.outputs['BSDF'], output.inputs['Surface'])
    
elif '{material_type}' == 'emission':
    # Emission material
    emission = nodes.new('ShaderNodeEmission')
    emission.location = (0, 0)
    emission.inputs['Color'].default_value = (1, 0.2, 0.2, 1)
    emission.inputs['Strength'].default_value = 5
    links.new(emission.outputs['Emission'], output.inputs['Surface'])
    
elif '{material_type}' == 'glass':
    # Glass material
    principled = nodes.new('ShaderNodeBsdfPrincipled')
    principled.location = (0, 0)
    principled.inputs['Transmission'].default_value = 1.0
    principled.inputs['Roughness'].default_value = 0.0
    principled.inputs['IOR'].default_value = 1.45
    links.new(principled.outputs['BSDF'], output.inputs['Surface'])
    
elif '{material_type}' == 'metallic':
    # Metallic material
    principled = nodes.new('ShaderNodeBsdfPrincipled')
    principled.location = (0, 0)
    principled.inputs['Metallic'].default_value = 1.0
    principled.inputs['Roughness'].default_value = 0.2
    links.new(principled.outputs['BSDF'], output.inputs['Surface'])
    
elif '{material_type}' == 'wood':
    # Procedural wood material
    principled = nodes.new('ShaderNodeBsdfPrincipled')
    principled.location = (0, 0)
    principled.inputs['Base Color'].default_value = (0.4, 0.2, 0.1, 1)
    principled.inputs['Roughness'].default_value = 0.7
    links.new(principled.outputs['BSDF'], output.inputs['Surface'])
    
else:
    # Default principled
    principled = nodes.new('ShaderNodeBsdfPrincipled')
    principled.location = (0, 0)
    links.new(principled.outputs['BSDF'], output.inputs['Surface'])

# Apply to selected object if exists
if bpy.context.active_object:
    if bpy.context.active_object.data:
        bpy.context.active_object.data.materials.append(mat)
    else:
        print("Active object has no material slot")
else:
    print("No active object to apply material")

print("Material '{name}' created with type: '{material_type}'")
"""
        
        args = self._get_blender_args(python_code=python_code)
        self._run_blender(args)
    
    def lighting(self, light_type: str = 'area', energy: float = 100, interactive: bool = False):
        """Setup lighting in the scene."""
        python_code = f"""
import bpy
import math

# Clear existing lights
bpy.ops.object.select_all(action='DESELECT')
for obj in bpy.data.objects:
    if obj.type == 'LIGHT':
        obj.select_set(True)

bpy.ops.object.delete()

# Create lighting based on type
if '{light_type}' == 'area':
    # Area light
    bpy.ops.object.light_add(type='AREA', location=(0, 0, 5))
    light = bpy.context.active_object
    light.data.energy = {energy}
    light.data.size = 5
    
elif '{light_type}' == 'sun':
    # Sun light
    bpy.ops.object.light_add(type='SUN', location=(0, 0, 10))
    light = bpy.context.active_object
    light.data.energy = {energy}
    light.rotation_euler = (math.radians(45), math.radians(0), math.radians(45))
    
elif '{light_type}' == 'point':
    # Point light
    bpy.ops.object.light_add(type='POINT', location=(3, 3, 3))
    light = bpy.context.active_object
    light.data.energy = {energy}
    
elif '{light_type}' == 'spot':
    # Spot light
    bpy.ops.object.light_add(type='SPOT', location=(0, 0, 5))
    light = bpy.context.active_object
    light.data.energy = {energy}
    light.data.spot_size = math.radians(45)
    
elif '{light_type}' == 'three-point':
    # Three-point lighting setup
    # Key light
    bpy.ops.object.light_add(type='AREA', location=(5, 5, 5))
    key_light = bpy.context.active_object
    key_light.data.energy = {energy}
    key_light.rotation_euler = (math.radians(-45), 0, math.radians(45))
    
    # Fill light
    bpy.ops.object.light_add(type='AREA', location=(-5, 0, 3))
    fill_light = bpy.context.active_object
    fill_light.data.energy = {energy} * 0.5
    
    # Back light
    bpy.ops.object.light_add(type='AREA', location=(0, -5, 4))
    back_light = bpy.context.active_object
    back_light.data.energy = {energy} * 0.3
    
elif '{light_type}' == 'hdri':
    # HDRI lighting (placeholder - would require actual HDRI file)
    world = bpy.context.scene.world
    if world is None:
        world = bpy.data.worlds.new('World')
        bpy.context.scene.world = world
    
    world.use_nodes = True
    nodes = world.node_tree.nodes
    nodes.clear()
    
    # This is a placeholder - real HDRI requires environment texture
    output = nodes.new('ShaderNodeOutputWorld')
    output.location = (0, 0)
    
else:
    # Default area light
    bpy.ops.object.light_add(type='AREA', location=(0, 0, 5))
    light = bpy.context.active_object
    light.data.energy = {energy}

print("Lighting setup complete with type: '{light_type}', energy: {energy}")
"""
        
        args = self._get_blender_args(python_code=python_code)
        self._run_blender(args)
    
    def camera(self, camera_type: str = 'perspective', position: tuple = None, interactive: bool = False):
        """Setup camera in the scene."""
        pos_x, pos_y, pos_z = position if position else (0, -10, 5)
        
        python_code = f"""
import bpy
import math

# Clear existing cameras
bpy.ops.object.select_all(action='DESELECT')
for obj in bpy.data.objects:
    if obj.type == 'CAMERA':
        obj.select_set(True)

bpy.ops.object.delete()

# Create camera
bpy.ops.object.camera_add(location=({pos_x}, {pos_y}, {pos_z}))

camera = bpy.context.active_object
bpy.context.scene.camera = camera

# Setup camera based on type
if '{camera_type}' == 'perspective':
    camera.data.type = 'PERSP'
    
elif '{camera_type}' == 'orthographic':
    camera.data.type = 'ORTHO'
    camera.data.ortho_scale = 10
    
elif '{camera_type}' == 'fisheye':
    camera.data.type = 'FISHEYE'
    camera.data.fisheye_fov = math.radians(180)
    
elif '{camera_type}' == 'panoramic':
    camera.data.type = 'PANORAMA'
    camera.data.panorama_type = 'EQUIRECTANGULAR'
    
else:
    camera.data.type = 'PERSP'

# Look at origin
direction = camera.location
rot_quat = direction.to_track_quat('-Z', 'Y')
camera.rotation_euler = rot_quat.to_euler()

print("Camera setup complete with type: '{camera_type}' at position: ({pos_x}, {pos_y}, {pos_z})")
"""
        
        args = self._get_blender_args(python_code=python_code)
        self._run_blender(args)
    
    def render(self, engine: str = 'cycles', samples: int = 128, output_path: str = '/tmp/render.png', interactive: bool = False):
        """Render the scene."""
        python_code = f"""
import bpy
import os

# Set render engine
bpy.context.scene.render.engine = '{engine}'

# Set samples
if '{engine}' == 'CYCLES':
    bpy.context.scene.cycles.samples = {samples}
    bpy.context.scene.cycles.device = 'CPU'
    
elif '{engine}' == 'BLENDER_EEVEE':
    bpy.context.scene.eevee.taa_render_samples = {samples}

# Set output settings
bpy.context.scene.render.resolution_x = 1920
bpy.context.scene.render.resolution_y = 1080
bpy.context.scene.render.filepath = '{output_path}'

# Set file format
if '{output_path}'.endswith('.png'):
    bpy.context.scene.render.image_settings.file_format = 'PNG'
elif '{output_path}'.endswith('.exr'):
    bpy.context.scene.render.image_settings.file_format = 'OPEN_EXR'

# Render
bpy.ops.render.render(write_still=True)

print(f"Render complete using {engine} engine with {samples} samples")
print(f"Output saved to: {{'{output_path}'}}")
"""
        
        args = self._get_blender_args(python_code=python_code)
        self._run_blender(args)
    
    def export(self, format: str = 'obj', output_path: str = '/tmp/export', interactive: bool = False):
        """Export the scene to various formats."""
        python_code = f"""
import bpy
import os

# Ensure output directory exists
output_dir = os.path.dirname('{output_path}')
if output_dir and not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Export based on format
if '{format}' == 'obj':
    bpy.ops.export_scene.obj(
        filepath='{output_path}.obj',
        use_selection=False,
        use_normals=True,
        use_triangles=True,
        use_materials=True
    )
    print(f"Exported to OBJ format: {{'{output_path}.obj'}}")
    
elif '{format}' == 'fbx':
    bpy.ops.export_scene.fbx(
        filepath='{output_path}.fbx',
        use_selection=False,
        bake_anim=False
    )
    print(f"Exported to FBX format: {{'{output_path}.fbx'}}")
    
elif '{format}' == 'gltf':
    bpy.ops.export_scene.gltf(
        filepath='{output_path}.glb',
        export_format='GLB',
        use_selection=False
    )
    print(f"Exported to glTF format: {{'{output_path}.glb'}}")
    
elif '{format}' == 'usd':
    bpy.ops.wm.usd_export(
        filepath='{output_path}.usd',
        export_selected=False
    )
    print(f"Exported to USD format: {{'{output_path}.usd'}}")
    
elif '{format}' == 'stl':
    bpy.ops.export_mesh.stl(
        filepath='{output_path}.stl',
        use_selection=False
    )
    print(f"Exported to STL format: {{'{output_path}.stl'}}")
    
else:
    print(f"Unsupported export format: '{format}'")
    print("Supported formats: obj, fbx, gltf, usd, stl")
"""
        
        args = self._get_blender_args(python_code=python_code)
        self._run_blender(args)
    
    def reset(self, interactive: bool = False):
        """Reset the Blender scene."""
        python_code = """
import bpy

# Clear all objects
bpy.ops.object.select_all(action='SELECT')
bpy.ops.object.delete(use_global=False)

# Clear all materials
for mat in bpy.data.materials:
    bpy.data.materials.remove(mat)

# Clear all meshes
for mesh in bpy.data.meshes:
    bpy.data.meshes.remove(mesh)

# Clear all lights
for light in bpy.data.lights:
    bpy.data.lights.remove(light)

# Clear all cameras
for camera in bpy.data.cameras:
    bpy.data.cameras.remove(camera)

# Reset scene settings
bpy.context.scene.render.engine = 'CYCLES'
bpy.context.scene.cycles.samples = 128

print("Scene reset complete")
"""
        
        args = self._get_blender_args(python_code=python_code)
        self._run_blender(args)
    
    def optimize(self, level: str = 'medium', interactive: bool = False):
        """Optimize the Blender scene."""
        python_code = f"""
import bpy

# Optimization based on level
if '{level}' == 'low':
    # Low optimization
    bpy.context.scene.render.engine = 'BLENDER_EEVEE'
    bpy.context.scene.eevee.taa_render_samples = 32
    bpy.context.scene.cycles.samples = 64
    bpy.context.scene.cycles.use_adaptive_sampling = True
    
elif '{level}' == 'medium':
    # Medium optimization
    bpy.context.scene.render.engine = 'CYCLES'
    bpy.context.scene.cycles.samples = 128
    bpy.context.scene.cycles.use_adaptive_sampling = True
    bpy.context.scene.cycles.blur_glossy = 0.5
    
elif '{level}' == 'high':
    # High optimization
    bpy.context.scene.render.engine = 'CYCLES'
    bpy.context.scene.cycles.samples = 256
    bpy.context.scene.cycles.use_adaptive_sampling = True
    bpy.context.scene.cycles.blur_glossy = 0.8
    bpy.context.scene.cycles.max_bounces = 4
    bpy.context.scene.cycles.diffuse_bounces = 2
    bpy.context.scene.cycles.glossy_bounces = 2
    bpy.context.scene.cycles.transmission_bounces = 2
    bpy.context.scene.cycles.volume_bounces = 0

# Optimize geometry
for obj in bpy.data.objects:
    if obj.type == 'MESH':
        # Apply decimation if mesh has too many polygons
        if len(obj.data.polygons) > 10000:
            bpy.context.view_layer.objects.active = obj
            bpy.ops.object.modifier_add(type='DECIMATE')
            obj.modifiers['Decimate'].ratio = 0.5
            bpy.ops.object.modifier_apply(modifier='Decimate')

print(f"Scene optimization complete at level: '{level}'")
"""
        
        args = self._get_blender_args(python_code=python_code)
        self._run_blender(args)
    
    def procedural(self, procedural_type: str = 'terrain', interactive: bool = False):
        """Create procedural content."""
        python_code = f"""
import bpy
import random
import math

# Clear existing
bpy.ops.object.select_all(action='SELECT')
bpy.ops.object.delete(use_global=False)

if '{procedural_type}' == 'terrain':
    # Procedural terrain
    bpy.ops.mesh.primitive_plane_add(size=20, location=(0, 0, 0))
    terrain = bpy.context.active_object
    
    # Add displacement modifier
    bpy.ops.object.modifier_add(type='DISPLACE')
    texture = bpy.data.textures.new('TerrainTexture', 'CLOUDS')
    texture.noise_scale = 2.0
    terrain.modifiers['Displace'].texture = texture
    terrain.modifiers['Displace'].strength = 2.0
    
    # Subdivide
    bpy.ops.object.modifier_add(type='SUBSURF')
    terrain.modifiers['Subdivision'].levels = 3
    
    # Smooth
    bpy.ops.object.shade_smooth()
    
    print("Procedural terrain created")
    
elif '{procedural_type}' == 'clouds':
    # Procedural clouds
    for i in range(5):
        x = random.uniform(-10, 10)
        y = random.uniform(-10, 10)
        z = random.uniform(5, 10)
        size = random.uniform(3, 6)
        
        bpy.ops.mesh.primitive_ico_sphere_add(radius=size, location=(x, y, z))
        cloud = bpy.context.active_object
        
        # Make transparent
        mat = bpy.data.materials.new(name=f'CloudMaterial{{i}}')
        mat.use_nodes = True
        mat.blend_method = 'BLEND'
        
        nodes = mat.node_tree.nodes
        principled = nodes.get('Principled BSDF')
        if principled:
            principled.inputs['Alpha'].default_value = 0.3
            
        cloud.data.materials.append(mat)
        bpy.ops.object.shade_smooth()
    
    print("Procedural clouds created")
    
elif '{procedural_type}' == 'water':
    # Procedural water
    bpy.ops.mesh.primitive_plane_add(size=30, location=(0, 0, 0))
    water = bpy.context.active_object
    
    # Create water material
    mat = bpy.data.materials.new(name='WaterMaterial')
    mat.use_nodes = True
    mat.blend_method = 'BLEND'
    
    nodes = mat.node_tree.nodes
    principled = nodes.get('Principled BSDF')
    if principled:
        principled.inputs['Base Color'].default_value = (0.1, 0.3, 0.5, 1)
        principled.inputs['Roughness'].default_value = 0.1
        principled.inputs['Transmission'].default_value = 1.0
        principled.inputs['IOR'].default_value = 1.33
    
    water.data.materials.append(mat)
    
    # Add waves
    bpy.ops.object.modifier_add(type='DISPLACE')
    texture = bpy.data.textures.new('WaterTexture', 'MUSGRAVE')
    texture.noise_scale = 1.0
    water.modifiers['Displace'].texture = texture
    water.modifiers['Displace'].strength = 0.5
    
    bpy.ops.object.shade_smooth()
    print("Procedural water created")
    
elif '{procedural_type}' == 'fractal':
    # Fractal pattern
    for i in range(50):
        x = i * 0.5 - 12.5
        y = math.sin(i * 0.5) * 3
        z = math.cos(i * 0.3) * 2
        
        bpy.ops.mesh.primitive_cube_add(size=0.3, location=(x, y, z))
        cube = bpy.context.active_object
        cube.rotation_euler.z = i * 0.1
        
        # Add emission material
        mat = bpy.data.materials.new(name=f'FractalMaterial{{i}}')
        mat.use_nodes = True
        nodes = mat.node_tree.nodes
        emission = nodes.new('ShaderNodeEmission')
        emission.inputs['Color'].default_value = (
            math.sin(i * 0.1) * 0.5 + 0.5,
            math.sin(i * 0.1 + 2) * 0.5 + 0.5,
            math.sin(i * 0.1 + 4) * 0.5 + 0.5,
            1
        )
        emission.inputs['Strength'].default_value = 3
        
        output = nodes.get('Material Output')
        if output:
            mat.node_tree.links.new(emission.outputs['Emission'], output.inputs['Surface'])
        
        cube.data.materials.append(mat)
    
    print("Procedural fractal created")
    
else:
    # Default procedural cube
    bpy.ops.mesh.primitive_cube_add(size=1, location=(0, 0, 0.5))
    print(f"Created default procedural object of type: '{procedural_type}'")

print(f"Procedural generation complete: '{{'{procedural_type}'}}'")
"""
        
        args = self._get_blender_args(python_code=python_code)
        self._run_blender(args)
    
    def run_file(self, file_path: str):
        """Run a Python script file in Blender."""
        if not os.path.exists(file_path):
            print(f"Error: File not found: {file_path}")
            return False
        
        args = self._get_blender_args(python_file=file_path)
        self._run_blender(args)
    
    def run_interactive(self):
        """Run in interactive mode."""
        print("Blender CLI Interactive Mode")
        print("Commands: build, material, lighting, camera, render, export, reset, optimize, procedural, quit")
        print("-" * 50)
        
        while True:
            try:
                command = input("blender> ").strip().split()
                
                if not command:
                    continue
                
                cmd = command[0].lower()
                
                if cmd == 'quit' or cmd == 'exit':
                    print("Goodbye!")
                    break
                
                elif cmd == 'build':
                    scene_type = command[1] if len(command) > 1 else 'default'
                    self.build(scene_type, interactive=True)
                
                elif cmd == 'material':
                    material_type = command[1] if len(command) > 1 else 'principled'
                    name = command[2] if len(command) > 2 else 'NewMaterial'
                    self.material(material_type, name, interactive=True)
                
                elif cmd == 'lighting':
                    light_type = command[1] if len(command) > 1 else 'area'
                    energy = float(command[2]) if len(command) > 2 else 100
                    self.lighting(light_type, energy, interactive=True)
                
                elif cmd == 'camera':
                    camera_type = command[1] if len(command) > 1 else 'perspective'
                    if len(command) > 4:
                        position = (float(command[2]), float(command[3]), float(command[4]))
                    else:
                        position = None
                    self.camera(camera_type, position, interactive=True)
                
                elif cmd == 'render':
                    engine = command[1] if len(command) > 1 else 'cycles'
                    samples = int(command[2]) if len(command) > 2 else 128
                    output_path = command[3] if len(command) > 3 else '/tmp/render.png'
                    self.render(engine, samples, output_path, interactive=True)
                
                elif cmd == 'export':
                    format = command[1] if len(command) > 1 else 'obj'
                    output_path = command[2] if len(command) > 2 else '/tmp/export'
                    self.export(format, output_path, interactive=True)
                
                elif cmd == 'reset':
                    self.reset(interactive=True)
                
                elif cmd == 'optimize':
                    level = command[1] if len(command) > 1 else 'medium'
                    self.optimize(level, interactive=True)
                
                elif cmd == 'procedural':
                    procedural_type = command[1] if len(command) > 1 else 'terrain'
                    self.procedural(procedural_type, interactive=True)
                
                else:
                    print(f"Unknown command: {cmd}")
                    print("Available commands: build, material, lighting, camera, render, export, reset, optimize, procedural, quit")
                
            except KeyboardInterrupt:
                print("\nGoodbye!")
                break
            except Exception as e:
                print(f"Error: {e}")
    
    def _run_blender(self, args: list):
        """Run Blender with given arguments."""
        try:
            result = subprocess.run(
                args,
                capture_output=True,
                text=True,
                timeout=120
            )
            
            if result.returncode == 0:
                print("Blender operation completed successfully")
                if result.stdout:
                    print(result.stdout)
            else:
                print(f"Blender operation failed with code: {result.returncode}")
                if result.stderr:
                    print(f"Error: {result.stderr}")
                    
        except subprocess.TimeoutExpired:
            print("Blender operation timed out")
        except Exception as e:
            print(f"Error running Blender: {e}")


def main():
    """Main entry point."""
    parser = argparse.ArgumentParser(
        description='Blender CLI Tool - Command-line interface for Blender operations',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s build                          # Build default scene
  %(prog)s build --type architectural     # Build architectural scene
  %(prog)s material --type metallic       # Create metallic material
  %(prog)s lighting --type three-point    # Setup three-point lighting
  %(prog)s camera --type orthographic     # Setup orthographic camera
  %(prog)s render --engine eevee          # Render with Eevee
  %(prog)s export --format obj            # Export to OBJ format
  %(prog)s optimize --level high          # High optimization
  %(prog)s procedural --type terrain      # Generate procedural terrain
  %(prog)s -i                             # Interactive mode
  %(prog)s --file script.py               # Run script file
  %(prog)s --python "import bpy"          # Run Python code
        """
    )
    
    # Main command
    parser.add_argument(
        'command',
        nargs='?',
        choices=['build', 'material', 'lighting', 'camera', 'render', 'export', 'reset', 'optimize', 'procedural'],
        help='Command to execute'
    )
    
    # Interactive mode
    parser.add_argument(
        '-i', '--interactive',
        action='store_true',
        help='Run in interactive mode'
    )
    
    # File mode
    parser.add_argument(
        '--file',
        metavar='FILE',
        help='Run Python script file in Blender'
    )
    
    # Python execution
    parser.add_argument(
        '--python',
        metavar='CODE',
        help='Execute Python code in Blender'
    )
    
    # Command-specific arguments
    parser.add_argument(
        '--type',
        metavar='TYPE',
        default='default',
        help='Type for build/material/lighting/camera/procedural commands'
    )
    
    parser.add_argument(
        '--name',
        metavar='NAME',
        default='NewMaterial',
        help='Name for material'
    )
    
    parser.add_argument(
        '--energy',
        type=float,
        default=100,
        help='Light energy (default: 100)'
    )
    
    parser.add_argument(
        '--engine',
        metavar='ENGINE',
        default='cycles',
        choices=['cycles', 'eevee', 'workbench'],
        help='Render engine (default: cycles)'
    )
    
    parser.add_argument(
        '--samples',
        type=int,
        default=128,
        help='Render samples (default: 128)'
    )
    
    parser.add_argument(
        '--format',
        metavar='FORMAT',
        default='obj',
        choices=['obj', 'fbx', 'gltf', 'usd', 'stl'],
        help='Export format (default: obj)'
    )
    
    parser.add_argument(
        '--output',
        metavar='PATH',
        default='/tmp/output',
        help='Output path for render/export'
    )
    
    parser.add_argument(
        '--level',
        metavar='LEVEL',
        default='medium',
        choices=['low', 'medium', 'high'],
        help='Optimization level (default: medium)'
    )
    
    parser.add_argument(
        '--position',
        nargs=3,
        type=float,
        metavar=('X', 'Y', 'Z'),
        help='Camera position (default: 0 -10 5)'
    )
    
    args = parser.parse_args()
    
    # Create tool instance
    tool = BlenderTool()
    
    # Handle modes
    if args.interactive:
        tool.run_interactive()
    elif args.file:
        tool.run_file(args.file)
    elif args.python:
        args_blender = tool._get_blender_args(python_code=args.python)
        tool._run_blender(args_blender)
    elif args.command:
        # Execute command
        if args.command == 'build':
            tool.build(args.type)
        elif args.command == 'material':
            tool.material(args.type, args.name)
        elif args.command == 'lighting':
            tool.lighting(args.type, args.energy)
        elif args.command == 'camera':
            tool.camera(args.type, args.position)
        elif args.command == 'render':
            tool.render(args.engine, args.samples, args.output)
        elif args.command == 'export':
            tool.export(args.format, args.output)
        elif args.command == 'reset':
            tool.reset()
        elif args.command == 'optimize':
            tool.optimize(args.level)
        elif args.command == 'procedural':
            tool.procedural(args.type)
    else:
        parser.print_help()


if __name__ == '__main__':
    main()
