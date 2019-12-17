from setuptools import setup, find_packages

setup(
    name='ctwseurat',
    version='0.1',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'Click', "rpy2", "ctwingest"
    ],
    entry_points='''
        [console_scripts]
        ctw-scanpy-obs=ctwseurat.cli:scanpy_obs
        ctw-from-seurat=ctwseurat.cli:from_seurat
        ctw-upload=ctwseurat.cli:upload_worksheet
    ''',
)
