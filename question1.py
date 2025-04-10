def calculate_actual_size(microscope_size, magnification):
    return microscope_size / magnification

# Example usage
microscope_size = float(input("Enter microscope size (e.g. 5.0 mm): "))
magnification = float(input("Enter magnification (e.g. 100x): "))
actual_size = calculate_actual_size(microscope_size, magnification)
print(f"Actual size of the specimen is {actual_size:.4f} mm")
