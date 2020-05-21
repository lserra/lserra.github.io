# Good Combination

good_combination = { m, d, c }

Ideas and thoughts about mathematics, data, coding. It's a good combination!

Stay in touch with us too.

Register in our site and receive our feeds.

## A professional and personal blog
[Build Status](https://travis-ci.org/ayushkumarshah/ayushkumarshah.github.io.svg?branch=source)

This repository hosts the code for my [blog](https://lserra.github.io/).

The website is powered by [Pelican](http://getpelican.com/) — a static site generator written in Python — and uses a theme based on [Flex](https://github.com/alexandrevicenzi/Flex.git).

### Build locally

The easiest way to do this in a Python is using [virtual environment](http://docs.python-guide.org/en/latest/dev/virtualenvs/).

### Create a Virtual Environment

Once you have `virtualenv` installed, create a virtual environment to hold Pelican and its dependencies:

```shell
$ virtualenv .venv
$ source .venv/bin/activate
```

This creates a virtual environment and then activates it. If you want to exit the virtual environment, type:

```shell
$ deactivate
```

### Fork / Clone the Repo

If you haven't already, clone your version of the repo:

```shell
$ git clone --recurse-submodules https://github.com/yourusername/repo/fork
```

### Install Pelican & Dependancies

Use `pip` to install the list of dependencies (including Pelican) into your virtual environment:

```shell
$ pip install -r requirements.txt
```

### Generate the Website

Now that the dependencies exists, we can build:

```shell
$ fab build
```

This takes the Markdown files from the `content/` directory and generates static HTML pages inside the `output/` directory. That's it. No database required.

### Preview the Website

You can serve the generated site so it can be previewed in your browser:

```shell
$ fab serve
```

And you can see the blog if you visit [http://localhost:8000](http://localhost:8000).

## Blog Workflow

If you're interested in writing a blog post for the website, you need to:

- [Fork]() the repository
- Write a blog post using Markdown in the `content` directory
- Push the changes to a topic branch, like `an-example-article`, on *your* fork of the repository
- Make a [pull request](https://help.github.com/articles/using-pull-requests/) against the `source` branch

## Hosting

This blog is hosted by [GitHub Pages](https://pages.github.com/). Also, I'm using continuous integration with [Travis](https://travis-ci.org) builds the site everytime the source is updated.

## License

The source code for generation of the blog is under [MIT License](https://github.com/ayushkumarshah/ayushkumarshah.github.io/blob/source/LICENSE.md). Content is copyrighted.

## Contact

If you have any questions, you can [email](mailto:laercio.serra@gmail.com) me.
