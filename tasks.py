"""
tasks.py — Automação de tarefas para o blog Good Combination.
Substitui o fabfile.py (Fabric 1.x), usando invoke (moderno e compatível com Python 3).

Uso:
    inv build       → Gera o site localmente
    inv rebuild     → Limpa e reconstrói tudo
    inv serve       → Serve em http://localhost:8000 com auto-reload
    inv preview     → Build de produção (publishconf.py)
    inv publish     → Deploy no GitHub Pages
"""

import shutil
from pathlib import Path

from invoke import task

# ─── Configuração ────────────────────────────────────────────────────────────

CONFIG = {
    "settings_base": "pelicanconf.py",
    "settings_publish": "publishconf.py",
    "deploy_path": Path("output"),
    "github_pages_branch": "master",
    "commit_message": "Publish site to GitHub Pages",
    "port": 8000,
}

# ─── Tarefas ─────────────────────────────────────────────────────────────────


@task
def clean(c):
    """Remove os arquivos gerados (pasta output/)."""
    deploy_path = CONFIG["deploy_path"]
    if deploy_path.is_dir():
        shutil.rmtree(deploy_path)
    deploy_path.mkdir(parents=True, exist_ok=True)
    print(f"✅ Pasta '{deploy_path}' limpa.")


@task
def build(c):
    """Gera o site localmente (modo desenvolvimento)."""
    c.run("pelican -s {settings_base}".format(**CONFIG))


@task
def rebuild(c):
    """Limpa tudo e reconstrói o site do zero."""
    clean(c)
    build(c)


@task
def regenerate(c):
    """Regenera automaticamente ao detectar mudanças nos arquivos."""
    c.run("pelican -r -s {settings_base}".format(**CONFIG))


@task
def serve(c):
    """Serve o site em http://localhost:8000/ com live-reload."""
    c.run(
        "pelican -lr -s {settings_base} -p {port}".format(**CONFIG)
    )


@task
def reserve(c):
    """Alias para `serve` (build + serve com live-reload)."""
    serve(c)


@task
def preview(c):
    """Gera a versão de produção do site (publishconf.py)."""
    c.run("pelican -s {settings_publish}".format(**CONFIG))


@task
def publish(c):
    """Faz o deploy automático no GitHub Pages (branch master)."""
    clean(c)
    c.run("pelican -s {settings_publish}".format(**CONFIG))
    c.run(
        'ghp-import -f -p -m "{commit_message}" -b {github_pages_branch} {deploy_path}'.format(
            **CONFIG
        )
    )
    print("🚀 Site publicado no GitHub Pages!")
