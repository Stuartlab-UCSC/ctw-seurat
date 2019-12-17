from setuptools import setup, find_packages

setup(
    name='ctw-seurat',
    version='0.1',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'Click', "scanpy==1.3.7", "scipy", "pandas", "rpy2",
        "beautifulsoup4", "requests", "requests_toolbelt", "urllib3==1.24.2"
    ],
    entry_points='''
        [console_scripts]
        ctw-scanpy-obs=ingest.cli:scanpy_obs
        ctw-from-seurat=ingest.cli:from_seurat
        ctw-upload=ingest.cli:upload_worksheet
    ''',
)
