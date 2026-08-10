import time
import torch
import torch_directml

device = torch_directml.device()
print(f"Device initialized: {device}\n")

print("Generating 4000x4000 matrices...")
a = torch.randint(1000, 10000, (4000, 4000), device=device)
b = torch.randint(1000, 10000, (4000, 4000), device=device)

# Warm-up run
_ = a @ b

print("Starting true synchronized measurement...")
start_time = time.time()

# 1. Multiply matrices
res = a @ b

# 2. FORCE SYNCHRONIZATION: By asking for a value from the result matrix, 
# the CPU is forced to wait until the GPU has fully completed the math.
_ = res[0, 0].item()

end_time = time.time()
elapsed_time_ms = (end_time - start_time) * 1000

print("Computation fully completed!")
print(f"True Execution Time: {elapsed_time_ms:.4f} milliseconds")