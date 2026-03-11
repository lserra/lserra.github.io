# Good Combination

`good_combination = { m, d, c }`

Blog pessoal sobre matemática, dados e código.

Este repositório contém o código-fonte de https://lserra.github.io, gerado com
[Pelican](https://getpelican.com/) e com tema [Flex](https://github.com/alexandrevicenzi/Flex).

## Tecnologias

- Python 3 + Pelican
- Pelican plugins (`pelican-plugins/`)
- Automacao de tarefas com Invoke (`tasks.py`)
- Publicacao no GitHub Pages com `ghp-import`

## Inicio rapido

Se voce ja criou e selecionou o virtualenv na IDE, execute:

```bash
pip install -r requirements.txt
python -m invoke --list
```

## Comandos do dia a dia (Invoke)

Este projeto usa `inv`/Invoke no lugar dos comandos antigos com `fab`.

```bash
inv clean       # remove os arquivos gerados em output/
inv build       # gera a versao de desenvolvimento
inv rebuild     # clean + build
inv regenerate  # monitora arquivos e regenera ao detectar mudancas
inv serve       # build + servidor com live reload na porta :8000
inv reserve     # alias para serve
inv preview     # build com publishconf.py
inv publish     # build + publicacao na branch do GitHub Pages
```

Acesse http://localhost:8000 apos `inv serve`.

## Estrutura do projeto

- `content/articles/`: posts do blog
- `content/pages/`: paginas estaticas (sobre, contato etc.)
- `content/images/`: imagens usadas por posts/paginas
- `output/`: site gerado (seguro recriar)
- `pelicanconf.py`: configuracao principal (desenvolvimento/padrao)
- `publishconf.py`: ajustes de producao
- `tasks.py`: ponto de entrada das tarefas Invoke

## Atualizar links sociais (incluindo LinkedIn)

Os links de perfis sociais ficam em `pelicanconf.py`, no bloco `SOCIAL`.

Para atualizar o LinkedIn, edite este item:

```python
('linkedin', 'https://www.linkedin.com/in/<your-profile>/'),
```

Em seguida, gere o site novamente:

```bash
inv build
```

## Fluxo de publicacao

`inv publish` executa:

1. limpa `output/`
2. gera com `publishconf.py`
3. executa `ghp-import` com push para a branch configurada (`master` em `tasks.py`)

Se a sua branch do Pages for `main` em vez de `master`, ajuste
`github_pages_branch` em `tasks.py`.

## CI/CD (GitHub Actions)

O deploy automatico foi migrado do Travis CI para GitHub Actions.

- Workflow: `.github/workflows/pelican-pages.yml`
- Build: executa em `push` e `pull_request` na branch `source`
- Deploy: executa apenas em `push` na branch `source`, usando `python -m invoke publish`

Configuracao recomendada no GitHub Pages:

- Source: `Deploy from a branch`
- Branch: `master`
- Folder: `/ (root)`

## Solucao de problemas

- `Unresolved reference 'invoke'` na IDE:
  garanta que o interpretador selecionado e o virtualenv do projeto e execute
  `pip install -r requirements.txt`.
- `inv: command not found`:
  use `python -m invoke <task>` em vez de `inv`.
- Comando do Pelican ausente durante tarefas:
  confirme que as dependencias foram instaladas no virtualenv ativo.

## Notas de legado

- `fabfile.py` existe por compatibilidade historica, mas o fluxo recomendado
  e `tasks.py` + Invoke.
- `fab` e bloqueado por design neste repositorio para evitar uso acidental de
  automacao depreciada; use os comandos `inv`.

## Licenca

O codigo-fonte esta sob licenca MIT (veja o arquivo de licenca do projeto).
O conteudo do blog permanece protegido por direitos autorais do autor.

## Contato

- Email: `laercio.serra@gmail.com`
