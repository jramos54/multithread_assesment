import threading
from utils.network import Network


def test_semaphore_limit():
    network = Network()
    max_concurrent_threads = 5
    counter = 0

    def worker():
        nonlocal counter
        with network.semaphore:
            counter += 1
            # Simulación de trabajo
            for _ in range(1000000):
                pass
            counter -= 1

    threads = []
    for _ in range(10):
        thread = threading.Thread(target=worker)
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    # Verificar que el número máximo de hilos concurrentes no se excedió
    assert counter <= max_concurrent_threads
