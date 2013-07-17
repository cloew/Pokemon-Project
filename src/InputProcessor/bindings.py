try:
    from pygame_bindings import keyBindings
    from pygame_bindings import keyStrings
except ImportError:
    from console_bindings import keyBindings
    from console_bindings import keyStrings

keyBindings = keyBindings
keyStrings = keyStrings