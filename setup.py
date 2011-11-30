#!/usr/bin/env python

from distutils.core import setup
from distutils.command.build_py import build_py
from distutils.spawn import find_executable
import os, os.path

class custom_build_py(build_py):
    def run(self):
        if True or not self.dry_run:
            antlr3 = None
            # First, try locally-hosted antlr3
            if os.path.exists('antlr-3.2.jar'):
                antlr3 = find_executable('java')
                if antlr3 is not None:
                    antlr3 = [antlr3, '-jar', 'antlr-3.2.jar']
            # Then, try to find system-provided one
            if antlr3 is None:
                antlr3 = find_executable('antlr3')
                if antlr3 is None:
                    raise RuntimeError("antlr3 (>= 3.2) is required to build")
                antlr3 = [antlr3]
            source_file = os.path.join('orderlyjson', 'OrderlyJSON.g')
            target_dir = os.path.join(self.build_lib, 'orderlyjson')
            tokens_file = os.path.join(target_dir, 'OrderlyJSON.tokens')
            self.mkpath(target_dir)
            self.spawn(antlr3 + ['-fo', target_dir, source_file])
            os.unlink(tokens_file)
        build_py.run(self)

setup(
    name='orderlyjson',
    version='1.0',
    description='A python implementation of Orderly JSON',
    long_description='Orderly is a textual format for describing JSON. '
                     'Orderly can be compiled into JSONSchema. '
                     'It is designed to be easy to read and write.',
    url='https://github.com/kroo/py-orderly-json',
    author='Elliot Kroo',
    author_email='elliot@kroo.net',
    #maintainer='Aleksey Zhukov',
    #maintainer_email='drdaeman@public.drdaeman.pp.ru',
    license='MIT',
    keywords=['Orderly', 'JSON'],
    platforms=['any'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries',
        'Operating System :: POSIX',
        'License :: OSI Approved :: MIT License',
    ],
    packages=['orderlyjson'],
    package_data={'orderlyjson': ['*.g']},
    data_files=[('share/doc/orderlyjson', ['README.md'])],
    scripts=['tools/orderly'],
    install_requires=['validictory>=0.7', 'antlr_python_runtime>=3.1'],
    cmdclass={'build_py': custom_build_py}
)
