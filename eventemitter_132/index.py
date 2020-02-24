# Write an event emitter that has three methods: on, emit, and removeListener.
# The `on` function takes in an event name and a callback function,
# the `emit` function takes in an event name and data (which will be passed to the associated callback),
# and `removeListener` takes in an event name and a callback to remove from that event.

from EventEmitter import EventEmitter


def test(args):
    print(args)


def test2(*args):
    print('should not run')


emitter = EventEmitter()

emitter.print_listeners()

emitter.on('my_event', test)
emitter.on('my_event', test2)

emitter.print_listeners()

emitter.remove_listener('my_event', test2)

emitter.print_listeners()

emitter.emit('my_event', 'hello', 'world')
