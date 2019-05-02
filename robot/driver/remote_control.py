class RemoteControl:
    def __init__(self, **kwargs):
        self.handler = kwargs["handler"]

    def start_listening(self):
        pass
        # https://stackoverflow.com/questions/7168508/background-function-in-python

    def received_command(self, command):
        self.handler.handle_remote_command(command)