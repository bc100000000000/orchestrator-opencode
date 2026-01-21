import bpy
import math
import time

# Clear existing objects
bpy.ops.object.select_all(action='SELECT')
bpy.ops.object.delete(use_global=False)

# Remove existing materials
for material in bpy.data.materials:
    bpy.data.materials.remove(material)

# Store step completion status
build_state = {
    "foundation": False,
    "walls": False,
    "roof": False,
    "windows": False,
    "door": False,
    "deck": False,
    "furniture": False,
    "lighting": False,
    "complete": False
}

def create_material(name, color, metallic=0.0, roughness=0.5):
    """Create a material with the given properties"""
    mat = bpy.data.materials.new(name=name)
    mat.use_nodes = True
    bsdf = mat.node_tree.nodes["Principled BSDF"]
    bsdf.inputs["Base Color"].default_value = color
    bsdf.inputs["Metallic"].default_value = metallic
    bsdf.inputs["Roughness"].default_value = roughness
    return mat

def step_foundations():
    """Step 1: Create the foundation/ground floor"""
    print("Step 1: Building foundations...")
    
    # Create foundation/floor
    bpy.ops.mesh.primitive_cube_add(size=2, location=(0, 0, 0.5))
    foundation = bpy.context.active_object
    foundation.name = "Foundation"
    foundation.scale = (6, 5, 0.3)
    
    mat = create_material("FoundationMat", (0.3, 0.3, 0.35, 1.0), metallic=0.1, roughness=0.8)
    foundation.data.materials.append(mat)
    
    build_state["foundation"] = True
    print("Foundation complete!")
    return 1.5  # Delay for 1.5 seconds

def step_walls():
    """Step 2: Create the walls"""
    print("Step 2: Building walls...")
    
    # Main house walls - concrete block style
    bpy.ops.mesh.primitive_cube_add(size=2, location=(0, 0, 2.5))
    walls = bpy.context.active_object
    walls.name = "Walls"
    walls.scale = (5.5, 4.5, 2.5)
    
    # Create a hole for the front door using boolean (simplified - just creating solid walls)
    mat = create_material("WallMat", (0.9, 0.9, 0.85, 1.0), metallic=0.0, roughness=0.9)
    walls.data.materials.append(mat)
    
    # Add some dimension with accent walls
    bpy.ops.mesh.primitive_cube_add(size=2, location=(-3, 2, 2.5))
    accent1 = bpy.context.active_object
    accent1.name = "AccentWall1"
    accent1.scale = (0.3, 0.5, 2.5)
    accent_mat = create_material("AccentMat1", (0.2, 0.25, 0.3, 1.0), metallic=0.2, roughness=0.4)
    accent1.data.materials.append(accent_mat)
    
    bpy.ops.mesh.primitive_cube_add(size=2, location=(3, 2, 2.5))
    accent2 = bpy.context.active_object
    accent2.name = "AccentWall2"
    accent2.scale = (0.3, 0.5, 2.5)
    accent2.data.materials.append(accent_mat)
    
    build_state["walls"] = True
    print("Walls complete!")
    return 1.5

def step_roof():
    """Step 3: Create the modern flat roof with overhang"""
    print("Step 3: Building roof...")
    
    # Flat roof with overhang
    bpy.ops.mesh.primitive_cube_add(size=2, location=(0, 0, 5.2))
    roof = bpy.context.active_object
    roof.name = "Roof"
    roof.scale = (6.5, 5.5, 0.2)
    
    mat = create_material("RoofMat", (0.15, 0.15, 0.18, 1.0), metallic=0.4, roughness=0.3)
    roof.data.materials.append(mat)
    
    # Roof trim/edge
    bpy.ops.mesh.primitive_cube_add(size=2, location=(0, 0, 5.0))
    trim = bpy.context.active_object
    trim.name = "RoofTrim"
    trim.scale = (6.7, 5.7, 0.15)
    trim_mat = create_material("TrimMat", (0.1, 0.1, 0.12, 1.0), metallic=0.5, roughness=0.2)
    trim.data.materials.append(trim_mat)
    
    build_state["roof"] = True
    print("Roof complete!")
    return 1.5

def step_windows():
    """Step 4: Add modern windows"""
    print("Step 4: Installing windows...")
    
    glass_mat = create_material("GlassMat", (0.6, 0.8, 0.9, 1.0), metallic=0.9, roughness=0.05)
    frame_mat = create_material("FrameMat", (0.1, 0.1, 0.1, 1.0), metallic=0.8, roughness=0.2)
    
    # Large front window
    bpy.ops.mesh.primitive_cube_add(size=2, location=(0, 2.3, 2.5))
    window1 = bpy.context.active_object
    window1.name = "FrontWindow"
    window1.scale = (3, 0.15, 1.8)
    window1.data.materials.append(glass_mat)
    
    # Window frame
    bpy.ops.mesh.primitive_cube_add(size=2, location=(0, 2.2, 2.5))
    frame1 = bpy.context.active_object
    frame1.name = "FrontWindowFrame"
    frame1.scale = (3.2, 0.05, 2.0)
    frame1.data.materials.append(frame_mat)
    
    # Side windows
    bpy.ops.mesh.primitive_cube_add(size=2, location=(-3, 0, 2.5))
    window2 = bpy.context.active_object
    window2.name = "LeftWindow"
    window2.scale = (0.15, 2, 1.5)
    window2.data.materials.append(glass_mat)
    
    bpy.ops.mesh.primitive_cube_add(size=2, location=(3, 0, 2.5))
    window3 = bpy.context.active_object
    window3.name = "RightWindow"
    window3.scale = (0.15, 2, 1.5)
    window3.data.materials.append(glass_mat)
    
    # Small window on side
    bpy.ops.mesh.primitive_cube_add(size=2, location=(-3, 0, 4))
    window4 = bpy.context.active_object
    window4.name = "AtticWindow"
    window4.scale = (0.15, 1.2, 0.8)
    window4.data.materials.append(glass_mat)
    
    build_state["windows"] = True
    print("Windows complete!")
    return 1.5

def step_door():
    """Step 5: Add the front door"""
    print("Step 5: Installing front door...")
    
    door_mat = create_material("DoorMat", (0.4, 0.25, 0.15, 1.0), metallic=0.1, roughness=0.6)
    handle_mat = create_material("HandleMat", (0.8, 0.8, 0.7, 1.0), metallic=0.9, roughness=0.1)
    
    # Front door
    bpy.ops.mesh.primitive_cube_add(size=2, location=(1.5, 2.3, 1.5))
    door = bpy.context.active_object
    door.name = "FrontDoor"
    door.scale = (1.2, 0.15, 1.5)
    door.data.materials.append(door_mat)
    
    # Door handle
    bpy.ops.mesh.primitive_cylinder_add(radius=0.05, depth=0.2, location=(2.1, 2.35, 1.3))
    handle = bpy.context.active_object
    handle.name = "DoorHandle"
    handle.rotation_euler = (0, math.pi/2, 0)
    handle.data.materials.append(handle_mat)
    
    # Door frame
    bpy.ops.mesh.primitive_cube_add(size=2, location=(1.5, 2.35, 1.5))
    frame = bpy.context.active_object
    frame.name = "DoorFrame"
    frame.scale = (1.4, 0.05, 1.7)
    frame.data.materials.append(handle_mat)
    
    build_state["door"] = True
    print("Door complete!")
    return 1.5

def step_deck():
    """Step 6: Add the deck/patio"""
    print("Step 6: Building deck...")
    
    deck_mat = create_material("DeckMat", (0.5, 0.35, 0.2, 1.0), metallic=0.0, roughness=0.7)
    
    # Main deck
    bpy.ops.mesh.primitive_cube_add(size=2, location=(1.5, 3.5, 0.9))
    deck = bpy.context.active_object
    deck.name = "Deck"
    deck.scale = (4, 1.5, 0.15)
    deck.data.materials.append(deck_mat)
    
    # Deck posts
    post_positions = [(-1, 3.5), (4, 3.5)]
    for i, pos in enumerate(post_positions):
        bpy.ops.mesh.primitive_cylinder_add(radius=0.08, depth=2, location=(pos[0], pos[1], 1.8))
        post = bpy.context.active_object
        post.name = f"DeckPost{i+1}"
        post_mat = create_material("PostMat", (0.9, 0.9, 0.9, 1.0), metallic=0.0, roughness=0.8)
        post.data.materials.append(post_mat)
    
    # Deck railing
    bpy.ops.mesh.primitive_cube_add(size=2, location=(1.5, 3.5, 2.5))
    railing = bpy.context.active_object
    railing.name = "DeckRailing"
    railing.scale = (4, 0.05, 0.1)
    railing.data.materials.append(post_mat)
    
    build_state["deck"] = True
    print("Deck complete!")
    return 1.5

def step_furniture():
    """Step 7: Add outdoor furniture"""
    print("Step 7: Adding furniture...")
    
    # Outdoor table
    bpy.ops.mesh.primitive_cylinder_add(radius=0.4, depth=0.05, location=(1.5, 3.5, 1.1))
    table_top = bpy.context.active_object
    table_top.name = "TableTop"
    table_mat = create_material("TableMat", (0.6, 0.5, 0.4, 1.0), metallic=0.0, roughness=0.7)
    table_top.data.materials.append(table_mat)
    
    # Table umbrella pole
    bpy.ops.mesh.primitive_cylinder_add(radius=0.03, depth=2, location=(1.5, 3.5, 2))
    umbrella_pole = bpy.context.active_object
    umbrella_pole.name = "UmbrellaPole"
    pole_mat = create_material("PoleMat", (0.8, 0.8, 0.8, 1.0), metallic=0.9, roughness=0.2)
    umbrella_pole.data.materials.append(pole_mat)
    
    # Umbrella top
    bpy.ops.mesh.primitive_cone_add(radius1=0.8, depth=0.3, location=(1.5, 3.5, 3.1))
    umbrella = bpy.context.active_object
    umbrella.name = "Umbrella"
    umbrella.scale = (1, 1, 0.8)
    umbrella_mat = create_material("UmbrellaMat", (0.9, 0.3, 0.2, 1.0), metallic=0.0, roughness=0.8)
    umbrella.data.materials.append(umbrella_mat)
    
    # Chairs
    chair_positions = [(0.8, 3.8), (0.8, 3.2), (2.2, 3.8)]
    chair_mat = create_material("ChairMat", (0.3, 0.4, 0.5, 1.0), metallic=0.0, roughness=0.8)
    
    for i, pos in enumerate(chair_positions):
        bpy.ops.mesh.primitive_cube_add(size=1, location=(pos[0], pos[1], 0.6))
        chair = bpy.context.active_object
        chair.name = f"Chair{i+1}"
        chair.scale = (0.5, 0.5, 0.6)
        chair.data.materials.append(chair_mat)
    
    build_state["furniture"] = True
    print("Furniture complete!")
    return 1.5

def step_lighting():
    """Step 8: Add lighting and camera"""
    print("Step 8: Setting up lighting and camera...")
    
    # Set up camera
    bpy.ops.object.camera_add(location=(15, -15, 12))
    camera = bpy.context.active_object
    camera.name = "MainCamera"
    camera.rotation_euler = (math.radians(60), 0, math.radians(45))
    bpy.context.scene.camera = camera
    
    # Add sun light
    bpy.ops.object.light_add(type='SUN', location=(10, -10, 20))
    sun = bpy.context.active_object
    sun.name = "Sun"
    sun.data.energy = 3
    
    # Add fill lights
    bpy.ops.object.light_add(type='POINT', location=(0, 0, 4))
    fill_light = bpy.context.active_object
    fill_light.name = "FillLight"
    fill_light.data.energy = 100
    fill_light.data.color = (1, 0.95, 0.9)
    
    # Add outdoor path lights
    for i, pos in enumerate([(-2, 5), (5, 5)]):
        bpy.ops.object.light_add(type='POINT', location=(pos[0], pos[1], 0.5))
        path_light = bpy.context.active_object
        path_light.name = f"PathLight{i+1}"
        path_light.data.energy = 50
        path_light.data.color = (1, 0.9, 0.7)
    
    # Set world background
    world = bpy.context.scene.world
    if not world:
        world = bpy.data.worlds.new("World")
        bpy.context.scene.world = world
    
    bg_node = world.node_tree.nodes["Background"]
    bg_node.inputs["Color"].default_value = (0.5, 0.7, 0.9, 1.0)
    bg_node.inputs["Strength"].default_value = 1.0
    
    build_state["lighting"] = True
    print("Lighting complete!")
    return 1.0

def step_complete():
    """Final step - mark as complete"""
    build_state["complete"] = True
    print("\n" + "="*50)
    print("MODERN HOUSE CONSTRUCTION COMPLETE!")
    print("="*50)
    print("\nBuild Summary:")
    for step, completed in build_state.items():
        status = "✓" if completed else "✗"
        print(f"  {status} {step.title()}")
    
    # Switch to rendered view
    for area in bpy.context.screen.areas:
        if area.type == 'VIEW_3D':
            for space in area.spaces:
                if space.type == 'VIEW_3D':
                    space.shading.type = 'RENDERED'
                    break
    
    return None  # No more steps

# Build steps with delays
build_steps = [
    step_foundations,
    step_walls,
    step_roof,
    step_windows,
    step_door,
    step_deck,
    step_furniture,
    step_lighting,
    step_complete
]

current_step = 0

def run_next_step():
    """Execute the next build step"""
    global current_step
    
    if current_step < len(build_steps):
        delay = build_steps[current_step]()
        current_step += 1
        if delay:
            return delay
    return None

# Start the build process
print("Starting modern house construction...")
print("Watch the house being built step by step!")
print("="*50)

# Register timer to run steps sequentially
bpy.app.timers.register(run_next_step, first_interval=2.0)
