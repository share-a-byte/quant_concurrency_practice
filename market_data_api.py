import time
import random
import threading

SYMBOLS = ["AAPL", "GOOG", "MSFT", "TSLA", "NVDA"]

def generate_tick():
    symbol = random.choice(SYMBOLS)
    price = round(random.uniform(100, 500), 2)
    timestamp = time.time()
    return {"symbol": symbol, "price": price, "timestamp": timestamp}

def start_market_data_stream(output_queue, stop_event, rate_per_sec=5):
    """
    Push simulated market data into output_queue at a controlled rate.
    Runs in its own thread. Call stop_event.set() to stop.
    Returns the producer thread so callers may optionally join it.
    """
    def stream():
        while not stop_event.is_set():
            tick = generate_tick()
            output_queue.put(tick)
            time.sleep(1 / rate_per_sec)

    producer_thread = threading.Thread(target=stream, daemon=True)
    producer_thread.start()
    return producer_thread

