import timeit as chronometer
import platform as machine
import psutil as system_info
import random as randomizer
import matplotlib.pyplot as vis

# Machine Specifications
def fetch_processor():
    return f"Processor: {machine.processor()}"

def fetch_memory():
    mem = system_info.virtual_memory()
    return f"Total Memory: {mem.total // (1024**3)} GB"

def fetch_drives():
    volumes = system_info.disk_partitions()
    storage_info = []
    for vol in volumes:
        try:
            usage = system_info.disk_usage(vol.mountpoint)
            storage_info.append(f"{vol.device} - Capacity: {usage.total // (1024**3)} GB, Available: {usage.free // (1024**3)} GB")
        except PermissionError:
            storage_info.append(f"{vol.device} - Not accessible")
    return storage_info

def fetch_os():
    return f"Operating System: {machine.system()} {machine.version()}"

# Sorting Algorithms
def arrange_by_insertion(data):
    for i in range(1, len(data)):
        key = data[i]
        j = i - 1
        while j >= 0 and data[j] > key:
            data[j + 1] = data[j]
            j -= 1
        data[j + 1] = key

def arrange_by_selection(data):
    for i in range(len(data)):
        min_idx = i
        for j in range(i+1, len(data)):
            if data[min_idx] > data[j]:
                min_idx = j
        data[i], data[min_idx] = data[min_idx], data[i]

def arrange_by_bubble(data):
    n = len(data)
    for i in range(n):
        for j in range(0, n-i-1):
            if data[j] > data[j+1]:
                data[j], data[j+1] = data[j+1], data[j]

def create_random_list(length):
    return [randomizer.randint(1, 1000) for _ in range(length)]

def measure_performance(algorithm, data):
    setup = f"from __main__ import {algorithm}, create_random_list; test_data = create_random_list({len(data)})"
    execution = f"{algorithm}(test_data)"
    return chronometer.timeit(execution, setup=setup, number=10)

# Test parameters
sample_sizes = [5, 10, 20, 50, 100, 200, 500, 1000, 2000]

# Performance results
performance_data = {
    'Insertion Sort': [],
    'Selection Sort': [],
    'Bubble Sort': []
}

# Conduct performance tests
for size in sample_sizes:
    test_list = create_random_list(size)

    performance_data['Insertion Sort'].append(measure_performance('arrange_by_insertion', test_list))
    performance_data['Selection Sort'].append(measure_performance('arrange_by_selection', test_list))
    performance_data['Bubble Sort'].append(measure_performance('arrange_by_bubble', test_list))

# Display system information
print("Machine Specifications:")
print(fetch_processor())
print(fetch_memory())
print(fetch_os())

print("\nStorage Information:")
for drive in fetch_drives():
    print(drive)

# Visualize results
vis.figure(figsize=(10, 6))
vis.plot(sample_sizes, performance_data['Insertion Sort'], label='Insertion Sort', marker='o')
vis.plot(sample_sizes, performance_data['Selection Sort'], label='Selection Sort', marker='s')
vis.plot(sample_sizes, performance_data['Bubble Sort'], label='Bubble Sort', marker='^')

vis.xlabel('List Size')
vis.ylabel('Execution Duration (seconds)')
vis.title('Sorting Algorithm Performance Comparison')
vis.legend()
vis.grid(True)
vis.show()