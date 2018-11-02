from distutils.core import  setup

import hylp

setup(
    name="hylp",
    version=hylp.__version__,
    description=hylp.__doc__.splitlines()[0],
    url="https://github.com/jalanb/hylp",
    requires=["argparse"],
    packages=["hylp"],
    scripts=["bin/hylp"],
    platforms='any',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Topic :: Software Development',
        'Topic :: Utilities'
    ],
    author="jalanb",
    author_email='github@al-got-rhythm.net',
)

