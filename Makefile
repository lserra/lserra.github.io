PY?=python3
PELICAN?=pelican
PELICANOPTS=

BASEDIR=$(CURDIR)
INPUTDIR=$(BASEDIR)/content
OUTPUTDIR=$(BASEDIR)/output
CONFFILE=$(BASEDIR)/pelicanconf.py
PUBLISHCONF=$(BASEDIR)/publishconf.py

SSH_HOST=localhost
SSH_PORT=22
SSH_USER=root
SSH_TARGET_DIR=/var/www

GITHUB_PAGES_BRANCH=master

DEBUG ?= 0
ifeq ($(DEBUG), 1)
	PELICANOPTS += -D
endif

RELATIVE ?= 0
ifeq ($(RELATIVE), 1)
	PELICANOPTS += --relative-urls
endif

help:
	@echo ''
	@echo 'Makefile for o blog Good Combination (Pelican 4.x + invoke)'
	@echo ''
	@echo 'Uso via invoke (recomendado):'
	@echo '   inv build         Gera o site localmente'
	@echo '   inv rebuild       Limpa e reconstrói tudo'
	@echo '   inv serve         Serve em http://localhost:8000 com live-reload'
	@echo '   inv preview       Build de produção (publishconf.py)'
	@echo '   inv publish       Deploy no GitHub Pages'
	@echo ''
	@echo 'Uso via make (alternativo):'
	@echo '   make html         (re)gera o site'
	@echo '   make clean        Remove os arquivos gerados'
	@echo '   make regenerate   Regenera ao detectar mudanças'
	@echo '   make serve        Serve em http://localhost:8000'
	@echo '   make publish      Gera usando configurações de produção'
	@echo '   make github       Deploy no GitHub Pages via ghp-import'
	@echo '   make rsync_upload Upload via rsync+ssh'
	@echo ''
	@echo 'Variáveis:'
	@echo '   DEBUG=1    Habilita modo debug'
	@echo '   RELATIVE=1 Habilita URLs relativas'
	@echo ''

html:
	$(PELICAN) $(INPUTDIR) -o $(OUTPUTDIR) -s $(CONFFILE) $(PELICANOPTS)

clean:
	[ ! -d $(OUTPUTDIR) ] || rm -rf $(OUTPUTDIR)

regenerate:
	$(PELICAN) -r $(INPUTDIR) -o $(OUTPUTDIR) -s $(CONFFILE) $(PELICANOPTS)

serve:
ifdef PORT
	$(PELICAN) -lr $(INPUTDIR) -o $(OUTPUTDIR) -s $(CONFFILE) -p $(PORT) $(PELICANOPTS)
else
	$(PELICAN) -lr $(INPUTDIR) -o $(OUTPUTDIR) -s $(CONFFILE) -p 8000 $(PELICANOPTS)
endif

publish:
	$(PELICAN) $(INPUTDIR) -o $(OUTPUTDIR) -s $(PUBLISHCONF) $(PELICANOPTS)

rsync_upload: publish
	rsync -e "ssh -p $(SSH_PORT)" -P -rvzc --delete $(OUTPUTDIR)/ $(SSH_USER)@$(SSH_HOST):$(SSH_TARGET_DIR) --cvs-exclude

github: publish
	ghp-import -m "Publish site to GitHub Pages" -b $(GITHUB_PAGES_BRANCH) $(OUTPUTDIR)
	git push origin $(GITHUB_PAGES_BRANCH)

.PHONY: html help clean regenerate serve publish rsync_upload github
