from cleo import Command


class Halo(Command):
    """
    Greets someone

    demo:greet
        {name? : Who do you want to greet?}
        {--y|yell : If set, the task will yell in uppercase letters}
    """

    def handle(self):
        name = self.argument('name')

        if name:
            text = 'Hello %s' % name
        else:
            text = 'Hello'

        if self.option('yell'):
            text = text.upper()

        self.line(text)
