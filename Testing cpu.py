import sys
import time

print("Starting memory stress test...")
print("Press Ctrl + C at any time to stop (Kill Switch).\n")

# A list to store our massive counting data
storage_list = []
range_limit = 100_000

try:
    count = 0
    while True:
        # Generate a large chunk of numbers and add it to the list
        batch = [str(i) for i in range(range_limit)]
        storage_list.append(batch)
        
        count += 1
        
        # Calculate approximate memory usage in Megabytes (MB)
        total_memory_bytes = sys.getsizeof(storage_list)
        for b in storage_list:
            total_memory_bytes += sys.getsizeof(b)
            
        memory_mb = total_memory_bytes / (1024 * 1024)
        
        print(f"Batches stored: {count} | Current RAM consumed by list: {memory_mb:.2f} MB")
        
        # Safety valve: Stop automatically if it reaches 1000 MB (1 GB)
        if memory_mb > 1000:
            print("\n[Safety Trigger] Reached 1 GB limit. Stopping safely.")
            break
            
        # Slight pause so you can watch it run
        time.sleep(0.1)

except KeyboardInterrupt:
    # This block activates instantly when you press Ctrl + C
    print("\n\n[Kill Switch Activated!] You interrupted the program.")

print("Cleaning up memory and exiting safely...")
# Clearing the list frees the RAM back up to your computer
storage_list.clear()
print("Done! RAM has been released.")
