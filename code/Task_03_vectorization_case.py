# Task 3 (related case): Normalising and gamma-correcting the pixels of a grey-scale image
import numpy as np
import timeit

rng = np.random.default_rng(42)
# A 1000 x 1000 grey image = 1,000,000 pixels with brightness 0-255
image = rng.integers(0, 256, size=(1000, 1000), dtype=np.uint8)

def loop_version():
    result = []
    for value in image.ravel():
        normalised = value / 255.0           # scale 0-255 to 0-1
        result.append(normalised ** 2.2)     # gamma correction
    return result

def vectorized_version():
    return (image / 255.0) ** 2.2

loop_time = timeit.timeit(loop_version, number=1)
vector_time = timeit.timeit(vectorized_version, number=3) / 3

corrected = vectorized_version()

print(f"Mean brightness before: {image.mean() / 255.0:.4f} (scaled to 0-1)")
print(f"Mean brightness after gamma 2.2: {corrected.mean():.4f}")
print(f"Loop time: {loop_time:.4f} s")
print(f"Vectorized time: {vector_time:.4f} s")
print(f"Approximate speed-up: {loop_time / vector_time:.1f}x")
