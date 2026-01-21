"""
Preview module for Blender Engine.
Handles rendering previews and display of 3D content.
"""

import bpy
import os
from pathlib import Path

class BlenderPreview:
    """Handles preview rendering and display for the Blender engine."""
    
    def __init__(self):
        """Initialize the preview system."""
        self.render_engine = 'CYCLES'
        self.resolution = (1920, 1080)
        self.output_format = 'PNG'
        
    def create_preview(self, object_name: str, camera_name: str = None) -> str:
        """
        Create a preview render of an object.
        
        Args:
            object_name: Name of the object to render
            camera_name: Optional camera to use for rendering
            
        Returns:
            Path to the rendered preview image
        """
        # Set up render settings
        bpy.context.scene.render.engine = self.render_engine
        bpy.context.scene.render.resolution_x = self.resolution[0]
        bpy.context.scene.render.resolution_y = self.resolution[1]
        bpy.context.scene.render.image_settings.file_format = self.output_format
        
        # Set output path
        output_path = Path.home() / "blender_previews" / f"{object_name}_preview"
        output_path.parent.mkdir(parents=True, exist_ok=True)
        
        bpy.context.scene.render.filepath = str(output_path)
        
        # Render the scene
        bpy.ops.render.render(write_still=True)
        
        return str(output_path)
    
    def set_resolution(self, width: int, height: int):
        """Set the preview resolution."""
        self.resolution = (width, height)
        
    def set_render_engine(self, engine: str):
        """Set the render engine to use."""
        self.render_engine = engine


def setup_preview_scene():
    """Set up a basic scene for previews."""
    # Create default camera
    bpy.ops.object.camera_add(location=(10, -10, 10))
    camera = bpy.context.active_object
    camera.rotation_euler = (0.785, 0, 0.785)  # 45 degrees
    bpy.context.scene.camera = camera
    
    # Set up lighting
    bpy.ops.object.light_add(type='SUN', location=(5, 5, 10))
    light = bpy.context.active_object
    light.data.energy = 3
    
    # Set world background
    world = bpy.context.scene.world
    if world is None:
        world = bpy.data.worlds.new('World')
        bpy.context.scene.world = world
    world.use_nodes = True
    bg_node = world.node_tree.nodes.get('Background')
    if bg_node:
        bg_node.inputs['Color'].default_value = (0.1, 0.1, 0.1, 1)


def render_quick_preview(object_name: str) -> str:
    """
    Quick preview render function.
    
    Args:
        object_name: Name of the object to render
        
    Returns:
        Path to the rendered preview
    """
    preview = BlenderPreview()
    preview.set_resolution(640, 480)
    return preview.create_preview(object_name)


# Main execution
if __name__ == "__main__":
    print("Blender Preview Module")
    print("Use create_preview(object_name) to render previews")
    print("Use setup_preview_scene() to initialize preview scene")
