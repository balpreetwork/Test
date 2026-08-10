import os
import time
import concurrent.futures

# Utilize a large chunk of your 24GB free space safely (e.g., 4 workers x 2GB = 8GB total files)
NUM_WORKERS = 4
FILE_SIZE_MB = 2000  # 2 GB per worker
CHUNK_SIZE = 4 * 1024 * 1024  # 4 MB chunks for heavy throughput

def stress_disk(worker_id):
    file_path = f"ssd_stress_{worker_id}.tmp"
    data_chunk = b"X" * CHUNK_SIZE
    total_chunks = FILE_SIZE_MB // 4  # Since chunk is 4MB

    try:
        while True:
            # Heavy Write
            with open(file_path, "wb", buffering=0) as f:
                for _ in range(total_chunks):
                    f.write(data_chunk)
            
            # Heavy Read
            with open(file_path, "rb", buffering=0) as f:
                while f.read(CHUNK_SIZE):
                    pass
    except Exception as e:
        print(f"Worker {worker_id} error: {e}")
    finally:
        if os.path.exists(file_path):
            os.remove(file_path)

print(f"--- Starting Multi-Threaded NVMe Stress Test ({NUM_WORKERS * FILE_SIZE_MB} MB active workload) ---")
print("Press Ctrl + C to stop.\n")

# Run multiple workers simultaneously using threads
try:
    with concurrent.futures.ThreadPoolExecutor(max_workers=NUM_WORKERS) as executor:
        executor.map(stress_disk, range(NUM_WORKERS))
except KeyboardInterrupt:
    print("\n--- Test Stopped. Cleaning up files... ---")