import renpy

import subprocess
import traceback

class Editor(renpy.editor.Editor):
    def begin(self, new_window=False, **kwargs):
        self.args = []

    def open(self, filename, line=None, **kwargs):
        if line:
            filename = "{}:{}".format(filename, line)
        self.args.extend(["-g", filename])

    has_projects = True

    def open_project(self, directory):
        self.args.extend(["-a", directory])

    def end(self, **kwargs):
        args = ["code"] + self.args + ['-r']
        if renpy.windows:
            args = ['cmd', '/c'] + args
            startupinfo = subprocess.STARTUPINFO()
            startupinfo.dwFlags = subprocess.CREATE_NEW_CONSOLE | subprocess.STARTF_USESHOWWINDOW
            startupinfo.wShowWindow = subprocess.SW_HIDE
        else:
            startupinfo = None
        args = [renpy.exports.fsencode(i) for i in args]

        subprocess.Popen(args, startupinfo=startupinfo)