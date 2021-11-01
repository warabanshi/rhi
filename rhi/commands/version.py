import pkg_resources

from rhi.commands.command import Command


class Version(Command):
    def invoke(self):
        ver = pkg_resources.get_distribution("rhi").version
        print(f"rhi-{ver}")
