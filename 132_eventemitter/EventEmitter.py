class EventEmitter:

    def __init__(self):
        self.listeners = {}

    def on(self, event, callback):
        if event not in self.listeners:
            self.listeners[event] = []

        self.listeners[event].append(callback)
        return

    def emit(self, event, *args):
        if event not in self.listeners:
            return

        for listener in self.listeners[event]:
            listener(args)

        return

    def print_listeners(self):
        for x, y in self.listeners.items():
            print(x)
            print(y)

        return

    def remove_listener(self, event, callback):
        if event not in self.listeners:
            return

        self.listeners[event].remove(callback)

        return

