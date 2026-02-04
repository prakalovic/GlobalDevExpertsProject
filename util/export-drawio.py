"""
Export Draw.io diagrams to PNG using the web version
"""
import subprocess
import os
from pathlib import Path

def export_drawio_to_png(drawio_file, output_file, scale=2, border=10, transparent=False):
    """
    Export a Draw.io file to PNG using the desktop app
    
    Args:
        drawio_file: Path to the .drawio file
        output_file: Path for the output PNG file
        scale: Resolution scale factor (1=100%, 2=200%, 3=300%, etc.)
        border: Border padding in pixels
        transparent: Use transparent background
    """
    drawio_exe = r"C:\Program Files\draw.io\draw.io.exe"
    
    if not os.path.exists(drawio_exe):
        print(f"Error: Draw.io not found at {drawio_exe}")
        return False
    
    # Convert to absolute paths
    drawio_path = Path(drawio_file).resolve()
    output_path = Path(output_file).resolve()
    
    # Create output directory if it doesn't exist
    output_path.parent.mkdir(parents=True, exist_ok=True)
    
    # Run draw.io with export parameters
    cmd = [
        drawio_exe,
        "--export",
        "--format", "png",
        "--scale", str(scale),
        "--border", str(border),
        "--output", str(output_path),
        str(drawio_path)
    ]
    
    if transparent:
        cmd.insert(2, "--transparent")
    
    print(f"Exporting {drawio_path} to {output_path}...")
    print(f"Command: {' '.join(cmd)}")
    
    try:
        result = subprocess.run(cmd, capture_output=True, text=True, timeout=30)
        
        if result.returncode == 0:
            print(f"✓ Successfully exported to {output_path}")
            return True
        else:
            print(f"✗ Export failed with code {result.returncode}")
            if result.stderr:
                print(f"Error: {result.stderr}")
            return False
    except subprocess.TimeoutExpired:
        print("✗ Export timed out after 30 seconds")
        return False
    except Exception as e:
        print(f"✗ Error: {e}")
        return False

if __name__ == "__main__":
    # Export the MS1 architecture diagram
    drawio_file = "docs/diagrams/MS1-architecture.drawio"
    output_file = "docs/diagrams/MS1-architecture.png"
    
    # Resolution options:
    # scale=1  -> 100% (normal resolution)
    # scale=2  -> 200% (high resolution) - recommended
    # scale=3  -> 300% (very high resolution)
    # scale=4  -> 400% (ultra high resolution)
    
    export_drawio_to_png(
        drawio_file, 
        output_file, 
        scale=3,           # Increase to 3x or 4x for higher resolution
        border=20,         # Add some padding around the diagram
        transparent=False  # Set to True for transparent background
    )
