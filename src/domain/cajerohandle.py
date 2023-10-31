from controller.cajerocontroller import Handler

class CajeroHandler(Handler):

    _next_handler: Handler = None

    def set_next(self, handler):
        self._next_handler = handler
        return handler

    def handle(self, monto):
        if self._next_handler:
            return self._next_handler.handle(monto)
        return None
