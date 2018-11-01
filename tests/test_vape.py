from unittest import TestCase
from cleo import Application, CommandTester

from vape import __version__
from vape.halo import Halo


def test_version():
    assert __version__ == '0.1.0'


class HaloTest(TestCase):

    def test_name_is_output(self):
        application = Application()
        application.add(Halo())

        command = application.find('demo:greet')
        command_tester = CommandTester(command)
        command_tester.execute([
            ('command', command.get_name()),
            ('name', 'John')
        ])

        self.assertRegex('Hello John\n', command_tester.get_display())
