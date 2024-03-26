from setuptools import setup, find_packages
setup(
    name='Witmotion16chServoDriverV2',
    version='0.1.0',
    author='Lidor Shimoni',
    author_email='lidor.shim@gmail.com',
    description='A driver for comminucating with Witmotion 16 channel servo microcontroller over Bluetooth + Serial',
    packages=find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)

