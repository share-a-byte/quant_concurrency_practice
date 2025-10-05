
cat > README.md <<'MD'
# Multithreaded Strategy Executor — HFT Exercise

This exercise simulates a simple HFT loop: a market-data producer pushes ticks into a queue, and your strategy runs in multiple threads to consume and process them.

## Files
- **`market_data_api.py`** — mock data producer. Do not modify.  
- **`strategy_executor.py`** — your work goes here. Implement the multithreaded consumers.  
- **`README.md`** — these instructions.

## Goal
Implement a strategy executor that:
1. Starts the provided market-data stream.
2. Launches **N worker threads** (e.g., 4).
3. Each worker repeatedly:
   - Pulls a tick from `data_queue`.
   - Simulates processing (e.g., `time.sleep(0.01)`).
   - Prints:  
     ```
     [Thread 0] Processed AAPL @ 432.10
     ```
   Use a `threading.Lock` to keep prints readable.
4. After a short run (a few seconds), shut down cleanly:
   - Signal the producer to stop.
   - Drain any remaining items.
   - Join worker threads.

## Hints
- Use `threading.Thread(target=..., args=(...))`.
- Use `queue.Queue()` for thread-safe handoff.
- `data_queue.get(timeout=1)` lets workers wake up to check for shutdown.
- Always call `data_queue.task_done()` after processing.
- Use `data_queue.join()` to wait until all queued items are processed.
- A shared `print_lock = threading.Lock()` avoids interleaved output.

## Stretch Ideas
- Measure latency from tick creation to processing.
- Use `concurrent.futures.ThreadPoolExecutor`.
- Run multiple producers to simulate multiple venues.

## Run
```bash
python strategy_executor.py

