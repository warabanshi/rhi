import importlib.metadata

from rhi.commands.command import Command


class Version(Command):
    def invoke(self):
        ver = importlib.metadata.version('rhi')
        print(f"rhi-{ver}")
