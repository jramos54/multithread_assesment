import threading


class Network:
    def __init__(self) -> None:
        # To limit the number of sensors in the network
        self.semaphore = threading.Semaphore(5)
