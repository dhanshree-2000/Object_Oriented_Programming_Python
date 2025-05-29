import multiprocessing
import sys

def process_function(number, output_queue):
    """Function that will be run by each process"""
    if number == 3:
        # Simulate failure for the 3rd process
        result = f"Process {number} failed (simulated)"
        output_queue.put(result)
        sys.exit(1)  # Exit with error code
    
    result = f"Process {number} completed successfully"
    output_queue.put(result)
    sys.exit(0)  # Exit successfully

def run_process_with_retries(number, output_queue):
    """Run a process and handle retries"""
    max_retries = 2
    
    for attempt in range(max_retries + 1):
        # Create and start the process
        p = multiprocessing.Process(
            target=process_function,
            args=(number, output_queue)
        )
        p.start()
        p.join()  # Wait for the process to complete
        
        if p.exitcode == 0:  # Success
            return
        elif attempt < max_retries:
            output_queue.put(f"Retrying process {number} (attempt {attempt + 1})")

def main():
    # Create a queue for inter-process communication
    output_queue = multiprocessing.Queue()
    
    # Create and start all processes
    processes = []
    for number in range(1, 6):
        p = multiprocessing.Process(
            target=run_process_with_retries,
            args=(number, output_queue)
        )
        processes.append(p)
        p.start()
    
    # Wait for all processes to complete
    for p in processes:
        p.join()
    
    # Print all output in order
    while not output_queue.empty():
        print(output_queue.get())

if __name__ == "__main__":
    main()