# task4_complete.py
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

def create_test_image():
    """Create a colorful test image for downsampling"""
    print("Creating synthetic test image...")
    
    height, width = 480, 640
    img = np.zeros((height, width, 3), dtype=np.uint8)
    
    # Create gradient background
    for i in range(height):
        for j in range(width):
            img[i, j, 0] = int((i / height) * 255)      # Red gradient
            img[i, j, 1] = int((j / width) * 255)       # Green gradient
            img[i, j, 2] = int(((i + j) / (height + width)) * 255)  # Blue gradient
    
    # Add shapes for better visualization
    for i in range(height):
        for j in range(width):
            # Red circle (center)
            if (i-240)**2 + (j-320)**2 < 100**2:
                img[i, j] = [255, 0, 0]
            # Green circle
            if (i-400)**2 + (j-200)**2 < 80**2:
                img[i, j] = [0, 255, 0]
            # Blue rectangle
            if 50 < i < 150 and 500 < j < 600:
                img[i, j] = [0, 0, 255]
            # White star pattern
            if abs(i-100) + abs(j-100) < 50:
                img[i, j] = [255, 255, 255]
    
    # Save as sample.jpg
    Image.fromarray(img).save("sample.jpg")
    print("✅ sample.jpg created successfully!")
    return img

def downsample_and_pixelate(image, N=8):
    """Perform spatial downsampling and pixelation"""
    print(f"\n=== DOWNSAMPLING ANALYSIS (N = {N}) ===")
    
    # Original image metrics
    print(f"Original Shape : {image.shape} | Memory: {image.nbytes:,} bytes")
    
    # Downsample using striding
    downsampled = image[::N, ::N, :]
    print(f"Downsampled Shape : {downsampled.shape} | Memory: {downsampled.nbytes:,} bytes")
    
    # Calculate reductions
    orig_h, orig_w = image.shape[0], image.shape[1]
    down_h, down_w = downsampled.shape[0], downsampled.shape[1]
    
    h_reduction = (1 - down_h / orig_h) * 100
    w_reduction = (1 - down_w / orig_w) * 100
    memory_savings = (1 - downsampled.nbytes / image.nbytes) * 100
    
    print(f"\nDimension Reduction: {h_reduction:.2f}% per axis")
    print(f"Memory Savings : {memory_savings:.2f}% data reduction")
    
    # Re-expand to original dimensions
    reexpanded = np.repeat(np.repeat(downsampled, N, axis=0), N, axis=1)
    
    if reexpanded.shape[0] > orig_h:
        reexpanded = reexpanded[:orig_h, :, :]
    if reexpanded.shape[1] > orig_w:
        reexpanded = reexpanded[:, :orig_w, :]
    
    print(f"Re-expanded Shape : {reexpanded.shape} | Visual: Blocky Pixelation")
    
    # Display results
    fig, axes = plt.subplots(1, 3, figsize=(15, 5))
    
    axes[0].imshow(image)
    axes[0].set_title(f'Original Image\n{orig_h}×{orig_w}', fontsize=12, fontweight='bold')
    axes[0].axis('off')
    
    axes[1].imshow(downsampled)
    axes[1].set_title(f'Downsampled (N={N})\n{down_h}×{down_w}', fontsize=12, fontweight='bold')
    axes[1].axis('off')
    
    axes[2].imshow(reexpanded)
    axes[2].set_title(f'Re-expanded (Pixelated)\n{reexpanded.shape[0]}×{reexpanded.shape[1]}', 
                      fontsize=12, fontweight='bold')
    axes[2].axis('off')
    
    plt.suptitle(f'Spatial Downsampling & Pixelation (Step Factor N={N})', 
                 fontsize=16, fontweight='bold')
    plt.tight_layout()
    
    # Save figure
    plt.savefig('downsampling_results.png', dpi=150, bbox_inches='tight')
    print("\n✅ Figure saved as: downsampling_results.png")
    
    plt.show()
    
    return downsampled, reexpanded

if __name__ == "__main__":
    try:
        # Try to load existing image
        print("Looking for sample.jpg...")
        img = Image.open("sample.jpg")
        image = np.array(img)
        print(f"✅ Loaded existing sample.jpg: {image.shape}")
    except FileNotFoundError:
        # Create synthetic image if not found
        print("⚠️ sample.jpg not found. Creating synthetic image...")
        image = create_test_image()
    
    # Run downsampling
    downsampled, pixelated = downsample_and_pixelate(image, N=8)
    print("\n✅ Task 4 completed successfully!")