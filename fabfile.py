import os
import shutil
import socketserver
import sys

import fabric.contrib.project as project
from fabric.api import *
from pelican.server import ComplexHTTPRequestHandler

# Local path configuration (can be absolute or relative to fabfile)
env.deploy_path = 'output'
env.msg = 'Update blog'
DEPLOY_PATH = env.deploy_path

# Remote server configuration
production = 'root@localhost:22'
dest_path = '/var/www'

# Rackspace Cloud Files configuration settings
env.cloudfiles_username = 'my_rackspace_username'
env.cloudfiles_api_key = 'my_rackspace_api_key'
env.cloudfiles_container = 'my_cloudfiles_container'

# Github Pages configuration
env.github_pages_branch = "master"

# Port for `serve`
SERVER = '127.0.0.1'
PORT = 8000


def clean():
    """Remove generated files"""
    if os.path.isdir(DEPLOY_PATH):
        shutil.rmtree(DEPLOY_PATH)
        os.makedirs(DEPLOY_PATH)


def build():
    """Build local version of site"""
    local('pelican -s pelicanconf.py')


def rebuild():
    """`build` with the delete switch"""
    clean()
    build()


def regenerate():
    """Automatically regenerate site upon file modification"""
    local('pelican -r -s pelicanconf.py')


def serve():
    """Serve site at http://localhost:8000/"""
    os.chdir(env.deploy_path)

    class AddressReuseTCPServer(socketserver.TCPServer):
        allow_reuse_address = True

    server = AddressReuseTCPServer(('', PORT), ComplexHTTPRequestHandler)

    sys.stderr.write('Serving on port {0} ...\n'.format(PORT))
    server.serve_forever()


def reserve():
    """`build`, then `serve`"""
    build()
    serve()


def preview():
    """Build production version of site"""
    local('pelican -s publishconf.py')


def publish():
    """Automatic deploy to GitHub Pages"""
    env.msg = "deploy and publish site"
    env.GH_TOKEN = os.getenv('GH_TOKEN')
    env.TRAVIS_REPO_SLUG = os.getenv('TRAVIS_REPO_SLUG')
    clean()
    build()
    with hide('running', 'stdout', 'stderr'):
        local("ghp-import -m '{msg}' -b {github_pages_branch} "
              "{deploy_path}".format(**env))
        local("git push -fq https://{GH_TOKEN}@github.com/"
              "{TRAVIS_REPO_SLUG}.git {github_pages_branch}".format(**env))

# def cf_upload():
#     """Publish to Rackspace Cloud Files"""
#     rebuild()
#     with lcd(DEPLOY_PATH):
#         local('swift -v -A https://auth.api.rackspacecloud.com/v1.0 '
#               '-U {cloudfiles_username} '
#               '-K {cloudfiles_api_key} '
#               'upload -c {cloudfiles_container} .'.format(**env))

# @hosts(production)
# def publish():
#     """Publish to production via rsync"""
#     local('pelican -s publishconf.py')
#     project.rsync_project(
#         remote_dir=dest_path,
#         exclude=".DS_Store",
#         local_dir=DEPLOY_PATH.rstrip('/') + '/',
#         delete=True,
#         extra_opts='-c',
#     )

# def gh_pages():
#     """Publish to GitHub Pages"""
#     rebuild()
#     local("ghp-import -b {github_pages_branch} {deploy_path} -p".format(**env))
#     local("ghp-import -b {github_pages_branch} {deploy_path} -p".format(**env))
