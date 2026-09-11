# task3_complete.py
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import os

def create_test_image():
    """Create a synthetic test image for channel extraction"""
    print("Creating synthetic test image...")
    
    # Create a colorful gradient image
    height, width = 480, 640
    image = np.zeros((height, width, 3), dtype=np.uint8)
    
    # Create gradients
    for i in range(height):
        for j in range(width):
            # Red gradient (top to bottom)
            image[i, j, 0] = int((i / height) * 255)
            # Green gradient (left to right)
            image[i, j, 1] = int((j / width) * 255)
            # Blue gradient (diagonal)
            image[i, j, 2] = int(((i + j) / (height + width)) * 255)
    
    # Add some shapes
    for i in range(height):
        for j in range(width):
            # Red circle (center)
            if (i-240)**2 + (j-320)**2 < 100**2:
                image[i, j] = [255, 0, 0]
            # Green circle
            if (i-400)**2 + (j-200)**2 < 80**2:
                image[i, j] = [0, 255, 0]
            # Blue rectangle
            if 50 < i < 150 and 500 < j < 600:
                image[i, j] = [0, 0, 255]
    
    return image

def analyze_channels():
    """Extract and display individual color channels"""
    print("\n" + "="*60)
    print("TASK 3: CHANNEL EXTRACTION ANALYSIS")
    print("="*60)
    
    # Create test image
    image = create_test_image()
    print(f"\nOriginal Image Shape : {image.shape}")
    
    # Extract individual channels
    red_channel = image[:, :, 0]
    green_channel = image[:, :, 1]
    blue_channel = image[:, :, 2]
    
    # Print statistics
    print(f"\nRed Channel 2D Shape : {red_channel.shape} | Mean Intensity: {np.mean(red_channel):.2f}")
    print(f"Green Channel 2D Shape: {green_channel.shape} | Mean Intensity: {np.mean(green_channel):.2f}")
    print(f"Blue Channel 2D Shape : {blue_channel.shape} | Mean Intensity: {np.mean(blue_channel):.2f}")
    
    # Create color-specific 3D arrays
    red_only = np.zeros_like(image)
    red_only[:, :, 0] = red_channel
    
    green_only = np.zeros_like(image)
    green_only[:, :, 1] = green_channel
    
    blue_only = np.zeros_like(image)
    blue_only[:, :, 2] = blue_channel
    
    # Visualization
    fig, axes = plt.subplots(2, 3, figsize=(15, 10))
    
    # Top Row: Color channels
    axes[0, 0].imshow(red_only)
    axes[0, 0].set_title('Red-Only Channel', fontsize=12, fontweight='bold')
    axes[0, 0].axis('off')
    
    axes[0, 1].imshow(green_only)
    axes[0, 1].set_title('Green-Only Channel', fontsize=12, fontweight='bold')
    axes[0, 1].axis('off')
    
    axes[0, 2].imshow(blue_only)
    axes[0, 2].set_title('Blue-Only Channel', fontsize=12, fontweight='bold')
    axes[0, 2].axis('off')
    
    # Bottom Row: Grayscale intensity maps
    axes[1, 0].imshow(red_channel, cmap='gray')
    axes[1, 0].set_title('Red Channel (Grayscale)', fontsize=12, fontweight='bold')
    axes[1, 0].axis('off')
    
    axes[1, 1].imshow(green_channel, cmap='gray')
    axes[1, 1].set_title('Green Channel (Grayscale)', fontsize=12, fontweight='bold')
    axes[1, 1].axis('off')
    
    axes[1, 2].imshow(blue_channel, cmap='gray')
    axes[1, 2].set_title('Blue Channel (Grayscale)', fontsize=12, fontweight='bold')
    axes[1, 2].axis('off')
    
    plt.suptitle('Color Channel Extraction & Visualization', fontsize=16, fontweight='bold')
    plt.tight_layout()
    
    # Save figure
    plt.savefig('channel_extraction.png', dpi=150, bbox_inches='tight')
    print("\n✅ Figure saved as: channel_extraction.png")
    
    plt.show()
    
    return image, red_channel, green_channel, blue_channel

if __name__ == "__main__":
    # Check if packages are installed
    try:
        import numpy as np
        import matplotlib.pyplot as plt
        from PIL import Image
        print("✅ All required packages are installed!")
    except ImportError as e:
        print(f"❌ Missing package: {e}")
        print("Please run: pip install numpy matplotlib pillow")
        exit()
    
    # Run channel extraction
    image, red, green, blue = analyze_channels()
    print("\n✅ Task 3 completed successfully!")