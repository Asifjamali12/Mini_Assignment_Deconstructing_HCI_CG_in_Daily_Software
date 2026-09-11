import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import os

# Check if packages are installed
try:
    import numpy as np
    import matplotlib.pyplot as plt
    from PIL import Image
    print("✓ All required packages are installed successfully!")
except ImportError as e:
    print(f"✗ Missing package: {e}")
    print("Please run: pip install numpy pillow matplotlib")

def create_synthetic_image():
    """
    Create a 300×400×3 synthetic image with colored quadrants.
    """
    print("\n=== SYNTHETIC IMAGE CREATION ===")
    
    # Create zero array
    height, width = 300, 400
    image = np.zeros((height, width, 3), dtype=np.uint8)
    
    # Fill quadrants using array slicing
    h_mid = height // 2
    w_mid = width // 2
    
    # Top-Left: Red [255, 0, 0]
    image[:h_mid, :w_mid] = [255, 0, 0]
    
    # Top-Right: Green [0, 255, 0]
    image[:h_mid, w_mid:] = [0, 255, 0]
    
    # Bottom-Left: Blue [0, 0, 255]
    image[h_mid:, :w_mid] = [0, 0, 255]
    
    # Bottom-Right: White [255, 255, 255]
    image[h_mid:, w_mid:] = [255, 255, 255]
    
    # Print matrix metrics
    print("\n--- SYNTHETIC MATRIX METRICS ---")
    print(f"Array Shape (H, W, C) : {image.shape}")
    print(f"Data Type : {image.dtype}")
    print(f"Total Elements : {image.size:,} values")
    print(f"Memory Footprint : {image.nbytes:,} bytes ({image.nbytes / 1024:.2f} KB)")
    
    # Display the image
    plt.figure(figsize=(8, 6))
    plt.imshow(image)
    plt.title(f'Synthetic 300×400×3 Image\nQuadrants: Red, Green, Blue, White')
    plt.axis('off')
    plt.tight_layout()
    plt.show()
    
    return image

# Create and display synthetic image
synthetic_img = create_synthetic_image()