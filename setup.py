from setuptools import setup, find_packages


setup(
    name='td_grpc_reader',
    version='0.6',
    license='MIT',
    author="Emre Yiğit",
    author_email='emre.yigit01@gmail.com',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    url='https://github.com/gmyrianthous/example-publish-pypi',
    keywords='example project',
    install_requires=[
        'urllib3',
        'grpcio-tools'
    ],

)