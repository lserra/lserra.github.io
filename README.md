# Good Combination

`good_combination = { m, d, c }`

Blog pessoal sobre matemática, dados e código.

Este repositório contém o código-fonte de https://lserra.github.io, gerado com
[Pelican](https://getpelican.com/) e com tema [Flex](https://github.com/alexandrevicenzi/Flex).

## Tecnologias

- Python 3 + Pelican
- Pelican plugins (`pelican-plugins/`)
- Automação de tarefas com Invoke (`tasks.py`)
- Publicação no GitHub Pages com `ghp-import`

## Início rápido

Se você já criou e selecionou o virtualenv na IDE, execute:

```bash
pip install -r requirements.txt
python -m invoke --list
```

## Comandos do dia a dia (Invoke)

Este projeto usa `inv`/Invoke no lugar dos comandos antigos com `fab`.

```bash
inv clean       # remove os arquivos gerados em output/
inv build       # gera a versão de desenvolvimento
inv rebuild     # clean + build
inv regenerate  # monitora arquivos e regenera ao detectar mudanças
inv serve       # build + servidor com live reload na porta :8000
inv reserve     # alias para serve
inv preview     # build com publishconf.py
inv publish     # build + publicação na branch do GitHub Pages
```

Acesse http://localhost:8000 após `inv serve`.

## Estrutura do projeto

- `content/articles/`: posts do blog
- `content/pages/`: páginas estáticas (sobre, contato etc.)
- `content/images/`: imagens usadas por posts/páginas
- `output/`: site gerado (seguro recriar)
- `custom-plugins/`: overrides locais para compatibilidade de plugins legados
- `pelicanconf.py`: configuração principal (desenvolvimento/padrão)
- `publishconf.py`: ajustes de produção
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

## Fluxo de publicação

`inv publish` executa:

1. limpa `output/`
2. gera com `publishconf.py`
3. executa `ghp-import` com push para a branch configurada (`master` em `tasks.py`)

Se a sua branch do Pages for `main` em vez de `master`, ajuste
`github_pages_branch` em `tasks.py`.

## Cheat sheet (rotina de publicação)

Use estes 6 comandos no fluxo diário (trabalho em `source`, deploy automático via GitHub Actions):

```bash
inv build
inv serve
git status
git add .
git commit -m "novo artigo: <titulo>"
git push origin source
```

## CI/CD (GitHub Actions)

O deploy automático foi migrado do Travis CI para GitHub Actions.

- Workflow: `.github/workflows/pelican-pages.yml`
- Build: executa em `push` e `pull_request` na branch `source`
- Deploy: executa apenas em `push` na branch `source`, usando `python -m invoke publish`

Configuração recomendada no GitHub Pages:

- Source: `Deploy from a branch`
- Branch: `master`
- Folder: `/ (root)`

## Solução de problemas

- `Unresolved reference 'invoke'` na IDE:
  garanta que o interpretador selecionado é o virtualenv do projeto e execute
  `pip install -r requirements.txt`.
- `inv: command not found`:
  use `python -m invoke <task>` em vez de `inv`.
- Comando do Pelican ausente durante tarefas:
  confirme que as dependências foram instaladas no virtualenv ativo.

## Notas de legado

- `fabfile.py` existe por compatibilidade histórica, mas o fluxo recomendado
  é `tasks.py` + Invoke.
- `fab` é bloqueado por design neste repositório para evitar uso acidental de
  automação depreciada; use os comandos `inv`.
- `custom-plugins/` existe para manter compatibilidade com plugins legados que
  não são totalmente compatíveis com as versões atuais de Python/Jinja2.

## Licença

O código-fonte está sob licença MIT (veja o arquivo de licença do projeto).
O conteúdo do blog permanece protegido por direitos autorais do autor.

## Contato

- Email: `laercio.serra@gmail.com`
