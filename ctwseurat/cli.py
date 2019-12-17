"""
cli exposed via flask
"""
import click
from ctwingest.webapi import upload, read_credentials
import ctwingest.scanpyapi as ad_obj
import ctwingest.scanpy_ingest as scanpy_ingest
from ctwseurat.seurat_api import rpy2Seurat3ToAnnData
import os


@click.command(help="Add a seurat object to the user file system")
@click.argument('worksheet_name')
@click.argument('s3')
@click.option('--cluster_name', default="louvain",
              help="The name of the key to the clustering solution in the seurat object, defaults to 'louvain'.")
@click.option('--celltype_key', default=None,
              help="The name of the key to the cell type annotation in the seurat object, defaults to None.")
def from_seurat(worksheet_name, s3, cluster_name,
                celltype_key=None
):
    print("reading in data...")
    ad = rpy2Seurat3ToAnnData(s3)
    scanpy_ingest(ad, worksheet_name, cluster_name, celltype_key)


@click.command(
    help="""Upload a worksheet to the UCSC Cell Atlas. Requires a credentials.json file filled with login info.
    Read the bottom of the README.md of the git repository.""")
@click.argument('ctw_path')
@click.argument('credentials_path')
@click.option('--group', "-g", default=None, help="A valid group name for the ctw server.")
@click.option('--url', "-u", default="https://cellatlasapi.ucsc.edu/",
              help="Only replace this if you are running your own ctw server.")
def upload_worksheet(ctw_path, credentials_path, url="https://cellatlasapi.ucsc.edu/", group=None):
    credentials = read_credentials(credentials_path)
    upload(ctw_path, credentials, url, group)


@click.command(help="See the keys for the scanpy observation matrix")
@click.argument('scanpy_path')
def scanpy_obs(scanpy_path):
    ad = ad_obj.readh5ad(scanpy_path)
    print(ad.obs_keys())

