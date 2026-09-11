import math

def calculate_display_metrics():
    """
    Calculate and classify display density based on physical screen attributes.
    """
    print("=== DISPLAY DENSITY CALCULATOR ===")
    print()
    
    # Get user input
    Wpx = int(input("Enter horizontal resolution (pixels): "))
    Hpx = int(input("Enter vertical resolution (pixels): "))
    Dinches = float(input("Enter physical diagonal size (inches): "))
    
    # Calculate total pixel count
    total_pixels = Wpx * Hpx
    
    # Calculate simplified aspect ratio
    gcd = math.gcd(Wpx, Hpx)
    aspect_w = Wpx // gcd
    aspect_h = Hpx // gcd
    
    # Calculate DPI/PPI
    diagonal_pixels = math.sqrt(Wpx**2 + Hpx**2)
    dpi = diagonal_pixels / Dinches
    
    # Classify display density
    if dpi < 100:
        category = "Low Density (Standard Monitor)"
    elif 100 <= dpi <= 200:
        category = "Medium Density (HD Display)"
    else:
        category = "High Density (Retina / Mobile)"
    
    # Display results
    print("\n--- DISPLAY METRICS ANALYSIS ---")
    print(f"Total Pixel Count : {total_pixels:,} pixels")
    print(f"Aspect Ratio : {aspect_w}:{aspect_h}")
    print(f"Calculated DPI : {dpi:.2f} DPI")
    print(f"Density Category : {category}")

# Test with different screen sizes
if __name__ == "__main__":
    # Desktop Monitor
    print("\n" + "="*50)
    print("TEST CASE 1: Desktop Monitor")
    print("="*50)
    Wpx, Hpx, Dinches = 1920, 1080, 24
    print(f"Input: {Wpx}×{Hpx}, {Dinches}\"")
    
    total_pixels = Wpx * Hpx
    gcd = math.gcd(Wpx, Hpx)
    aspect_w = Wpx // gcd
    aspect_h = Hpx // gcd
    diagonal_pixels = math.sqrt(Wpx**2 + Hpx**2)
    dpi = diagonal_pixels / Dinches
    
    if dpi < 100:
        category = "Low Density (Standard Monitor)"
    elif 100 <= dpi <= 200:
        category = "Medium Density (HD Display)"
    else:
        category = "High Density (Retina / Mobile)"
    
    print("\n--- DISPLAY METRICS ANALYSIS ---")
    print(f"Total Pixel Count : {total_pixels:,} pixels")
    print(f"Aspect Ratio : {aspect_w}:{aspect_h}")
    print(f"Calculated DPI : {dpi:.2f} DPI")
    print(f"Density Category : {category}")
    
    # Smartphone Screen
    print("\n" + "="*50)
    print("TEST CASE 2: Smartphone Screen")
    print("="*50)
    Wpx, Hpx, Dinches = 1170, 2532, 6.1
    print(f"Input: {Wpx}×{Hpx}, {Dinches}\"")
    
    total_pixels = Wpx * Hpx
    gcd = math.gcd(Wpx, Hpx)
    aspect_w = Wpx // gcd
    aspect_h = Hpx // gcd
    diagonal_pixels = math.sqrt(Wpx**2 + Hpx**2)
    dpi = diagonal_pixels / Dinches
    
    if dpi < 100:
        category = "Low Density (Standard Monitor)"
    elif 100 <= dpi <= 200:
        category = "Medium Density (HD Display)"
    else:
        category = "High Density (Retina / Mobile)"
    
    print("\n--- DISPLAY METRICS ANALYSIS ---")
    print(f"Total Pixel Count : {total_pixels:,} pixels")
    print(f"Aspect Ratio : {aspect_w}:{aspect_h}")
    print(f"Calculated DPI : {dpi:.2f} DPI")
    print(f"Density Category : {category}")