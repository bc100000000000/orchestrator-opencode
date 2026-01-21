"""
Blender Render Output Module
Handles render output paths, formats, and processing.
"""

import os
from pathlib import Path
from typing import Optional
from dataclasses import dataclass
from enum import Enum


class RenderFormat(Enum):
    """Supported render output formats."""
    PNG = "png"
    JPEG = "jpg"
    OPEN_EXR = "exr"
    TIFF = "tif"
    MPEG4 = "mp4"
    AVI = "avi"


@dataclass
class RenderSettings:
    """Configuration for render output."""
    output_path: Path
    format: RenderFormat = RenderFormat.PNG
    resolution_x: int = 1920
    resolution_y: int = 1080
    fps: int = 24
    compression: int = 90
    
    def get_extension(self) -> str:
        """Get file extension for current format."""
        format_extensions = {
            RenderFormat.PNG: ".png",
            RenderFormat.JPEG: ".jpg",
            RenderFormat.OPEN_EXR: ".exr",
            RenderFormat.TIFF: ".tif",
            RenderFormat.MPEG4: ".mp4",
            RenderFormat.AVI: ".avi",
        }
        return format_extensions.get(self.format, ".png")


class RenderOutput:
    """Manages Blender render output operations."""
    
    def __init__(self, settings: Optional[RenderSettings] = None):
        self.settings = settings or RenderSettings(
            output_path=Path.home() / "blender_renders"
        )
        self._ensure_output_directory()
    
    def _ensure_output_directory(self) -> None:
        """Create output directory if it doesn't exist."""
        self.settings.output_path.mkdir(parents=True, exist_ok=True)
    
    def get_output_path(self, filename: str) -> Path:
        """Generate full output path for a render."""
        extension = self.settings.get_extension()
        return self.settings.output_path / f"{filename}{extension}"
    
    def generate_frame_path(self, base_name: str, frame_number: int) -> Path:
        """Generate path for individual frame renders."""
        extension = self.settings.get_extension()
        frame_name = f"{base_name}_{frame_number:04d}"
        return self.settings.output_path / f"{frame_name}{extension}"
    
    def validate_settings(self) -> bool:
        """Validate current render settings."""
        if not self.settings.output_path.exists():
            return False
        
        valid_formats = [fmt.value for fmt in RenderFormat]
        if self.settings.format.value not in valid_formats:
            return False
        
        if self.settings.resolution_x <= 0 or self.settings.resolution_y <= 0:
            return False
        
        return True
    
    def get_format_string(self) -> str:
        """Get Blender-compatible format string."""
        format_mapping = {
            RenderFormat.PNG: "PNG",
            RenderFormat.JPEG: "JPEG",
            RenderFormat.OPEN_EXR: "OPEN_EXR",
            RenderFormat.TIFF: "TIFF",
            RenderFormat.MPEG4: "FFMPEG",
            RenderFormat.AVI: "AVI",
        }
        return format_mapping.get(self.settings.format, "PNG")
    
    def __repr__(self) -> str:
        return (
            f"RenderOutput(path={self.settings.output_path}, "
            f"format={self.settings.format.value}, "
            f"resolution={self.settings.resolution_x}x{self.settings.resolution_y})"
        )


def create_render_output(
    output_path: str,
    format: str = "png",
    resolution_x: int = 1920,
    resolution_y: int = 1080
) -> RenderOutput:
    """Factory function to create RenderOutput instance."""
    try:
        render_format = RenderFormat(format.lower())
    except ValueError:
        render_format = RenderFormat.PNG
    
    settings = RenderSettings(
        output_path=Path(output_path),
        format=render_format,
        resolution_x=resolution_x,
        resolution_y=resolution_y
    )
    
    return RenderOutput(settings)


if __name__ == "__main__":
    # Demo usage
    output = create_render_output(
        output_path="/tmp/blender_test",
        format="png",
        resolution_x=1920,
        resolution_y=1080
    )
    
    print(f"Created: {output}")
    print(f"Output path: {output.get_output_path('test_render')}")
    print(f"Valid: {output.validate_settings()}")
