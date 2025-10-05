import queue
import threading
import time

from market_data_api import start_market_data_stream

# Shared queue where market data arrives
data_queue = queue.Queue()

# Event to stop the data producer
stop_event = threading.Event()

# Lock for printing (so output doesn't interleave)
print_lock = threading.Lock()

# TODO: Implement this function
def strategy_worker(thread_id):
    """
    Continuously fetches data from the queue and processes it.
    Simulate some delay to represent strategy computation.
    Hints:
      - Use data_queue.get(timeout=...) to allow graceful exit.
      - Call data_queue.task_done() after processing each item.
      - Hold print_lock when printing.
    """
    pass  # <-- Replace this with your thread loop

# TODO: Implement this function
def main():
    num_threads = 4
    stream_duration = 5  # seconds

    # Start the mock data stream
    producer_thread = start_market_data_stream(data_queue, stop_event, rate_per_sec=10)

    # TODO: Create and start worker threads

    # Let the data stream run for a while
    time.sleep(stream_duration)

    # TODO: Signal stop to producer and wait for queue to finish
    # stop_event.set()
    # data_queue.join()

    # TODO: Join all threads
    # for t in threads: t.join()
    # Optionally join the producer:
    # producer_thread.join(timeout=1)

    print("All data processed.")

if __name__ == "__main__":
    main()

