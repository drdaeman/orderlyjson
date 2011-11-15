#!/usr/bin/env python

from distutils.core import setup
from distutils.command.build_py import build_py
import os.path

class custom_build_py(build_py):
    def run(self):
        if True or not self.dry_run:
            jar_file = 'antlr-3.2.jar'
            source_file = os.path.join('orderlyjson', 'OrderlyJSON.g')
            target_dir = os.path.join(self.build_lib, 'orderlyjson')
            tokens_file = os.path.join(self.build_lib, 'orderlyjson', 'OrderlyJSON.tokens')
            self.mkpath(target_dir)
            self.spawn(['java', '-jar', jar_file, '-fo', target_dir, source_file])
            os.unlink(tokens_file)
        build_py.run(self)

setup(
    name='orderlyjson',
    version='1.0',
    description='A python implementation of Orderly JSON',
    url='https://github.com/kroo/py-orderly-json',
    author='Elliot Kroo',
    author_email='elliot@kroo.net',
    license='MIT',
    keywords=['Orderly', 'JSON'],
    packages=['orderlyjson'],
    requires=['validictory (>= 0.7)', 'antlr3'],
    cmdclass={'build_py': custom_build_py}
)
