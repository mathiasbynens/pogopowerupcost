#!/usr/bin/env python
# coding=utf-8

from setuptools import setup

setup(
	name = 'pogopowerupcost',
	packages = ['pogopowerupcost'],
	version = '1.0.0',
	download_url = 'https://github.com/mathiasbynens/pogopowerupcost/tarball/v1.0.0',
	description = 'Easily calculate how much stardust and candy it takes to power-up a Pokémon from level `a` to level `b` in Pokémon GO.',
	classifiers=[
		'Development Status :: 5 - Production/Stable',
		'Intended Audience :: Developers',
		'License :: OSI Approved :: MIT License',
		'Operating System :: MacOS :: MacOS X',
		'Operating System :: Microsoft :: Windows',
		'Operating System :: POSIX :: Linux',
		'Operating System :: POSIX',
		'Programming Language :: Python :: 2.6',
		'Programming Language :: Python :: 2.7',
		'Programming Language :: Python :: 3.3',
		'Programming Language :: Python :: 3.4',
		'Programming Language :: Python :: 3.5',
		'Programming Language :: Python :: Implementation :: PyPy',
		'Topic :: Software Development :: Libraries',
	],
	author = 'Mathias Bynens',
	author_email = 'mathias@qiwi.be',
	license='MIT',
	url = 'https://github.com/mathiasbynens/pogopowerupcost',
	keywords = ['pogo', 'pokemon go', 'stardust', 'candy'],
	test_suite='nose.collector',
	tests_require=['nose'],
)
