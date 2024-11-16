import time
import multiprocessing

def stress_task(n):
    result = 0
    for i in range(n):
        result += i
    return result

start_time = time.time()

# Number of processes and iterations for each process
num_processes = 8  # You can increase this for more load
iterations_per_process = 10**7  # High number of iterations

# Create a pool of processes
with multiprocessing.Pool(processes=num_processes) as pool:
    results = pool.map(stress_task, [iterations_per_process] * num_processes)

end_time = time.time()

print(f"Stress test with {num_processes} processes completed.")
print(f"Time taken: {end_time - start_time:.2f} seconds.")
