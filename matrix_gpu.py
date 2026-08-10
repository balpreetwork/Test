import time
import torch
import torch_directml

# 1. Set up the DirectML device (Intel Integrated Graphics)
device = torch_directml.device()
print(f"Running benchmark on device: {device}\n")

# 2. Use a smaller size (like 4x4) if you want to see the actual numbers printed clearly, 
# or keep it large if you just want the shape. Let's use 4x4 for printing readability:
print("Generating 4x4 matrices...")
a = torch.randint(1000, 10000, (4, 4), device=device)
b = torch.randint(1000, 10000, (4, 4), device=device)

print("Starting performance measurement...")
start_time = time.time()

# 3. Matrix multiplication
res = a @ b

end_time = time.time()
elapsed_time_ms = (end_time - start_time) * 1000

# Print the matrices and results
print("Matrix A:\n", a)
print("\nMatrix B:\n", b)
print("\nFinal Result Matrix:\n", res)
print(f"\nExecution Time: {elapsed_time_ms:.4f} milliseconds")