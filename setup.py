from distutils.core import setup

setup(
    name='CricketMatch Simulator',
    version='0.1',
    author='Manish Bhatia',
    author_email='manishbhatias@gmail.com',
    url='https://github.com/manishbhatias/cricket-match-simulation',
    packages=['cricketmatch_simulator'],
    license='unlicense',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    install_requires=[
        "numpy >= 1.16.4"
    ],
)