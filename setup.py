from distutils.core import setup
from setuptools import find_packages

setup(
    name='6DOF_tracking_evaluation',
    version='0.1dev',
    packages=find_packages() + ['ulaval_6dof_object_tracking.deeptrack'],
    author='Mathieu Garon',
    author_email='mathieugaron91@gmail.com',
    requires=['numpy', 'Pillow', 'plyfile', 'pyopengl', 'vispy', 'seaborn', 'pandas']
)
