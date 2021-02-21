Title: Intro to Pelican and Github Pages
Date: 2021-02-19 11:00
Category: Python
Tags: pelican, publishing, github, markdown
Slug: getting-started-pelican
Authors: Ethan King
Summary: Summarizing the Pelican project

I've always liked the idea of hosting a website for free on [Github Pages](https://pages.github.com/). Having a 
preference for Python, I decided to use [Pelican](https://docs.getpelican.com/en/latest/) for the static website 
generation. I like the idea of using [markdown](https://www.markdownguide.org/basic-syntax/) to generate content. A 
healthy [theme selection](http://www.pelicanthemes.com/) to choose from, and using Github for deployment makes pushing 
changes a one-line command with 'make github'. This is a guide on hosting a static website on 
Github pages using Python, Pelican, and of course, Git. 

## Setting up the environment

Start off the project with creating the project directory. Having multiple directories will help organize the website 
content and any themes you wish to use. 
```bash
mkdir github_pages
cd github_pages
mkdir personal
cd personal
```

Create a virtual environment.
```bash
python3 -m venv env
activate virtual env
source env/bin/activate
deactivate
```

Install dependencies. More info can be found in [Pelican's offical docs](https://docs.getpelican.com/en/latest/install.html)
```bash
python3 -m pip install pelican
```

Now that the directory and python environment is setup, initialize the project with Pelican files with the 'pelican-
quickstart' command.
```bash
pelican-quickstart

yourproject/
├── content
│   └── (pages)
├── output
├── tasks.py
├── Makefile
├── pelicanconf.py       # Main settings file
└── publishconf.py       # Settings to use when ready to publish
```

initializing git
```bash
git init

git remote add origin https://github.com/MY_PROFILE/MY_REPO.git
git checkout dev

git add .
git commit -m 'Initialized Pelican'

git branch -a
```

## choosing a theme

Pelican's themes allow you to get a site up and running quickly. Once you figure out how to get the pages organized so 
Pelican can find them, managing a website becomes much easier.

Browsing throgh the available themes, the Pelican Blue theme really caught my eye due to its simplicity. The following 
pelicanconf and publishconf settings are used in the Pelican Blue theme. If you decide to use a different theme, 
different features may be available. Check out the theme's Github repo to see how to use the theme with your content.

Pull the repo locally and use the path in pelicanconf.py.
```bash
cd /Projects/github_pages
mkdir themes
cd themes
git clone https://github.com/ethan-king/pelican-blue.git
```


## setup using pelicanconf.py

This is the main settings file, and where we can understand what's going on in Pelican. This is where we can tell 
Pelican where our content is, what theme to use, social media info, etc.

pelicanconf.py
```python
THEME = '/Documents/Projects/github_pages/themes/pelican-blue'
SOCIAL = (('linkedin', 'https://www.linkedin.com/in/username'),
          ('github', 'https://github.com/username'),
          ('twitter', 'https://twitter.com/username'),
          )
SIDEBAR_DIGEST = 'Programmer and Web Developer'
FAVICON = 'url-to-favicon'
DISPLAY_PAGES_ON_MENU = True
TWITTER_USERNAME = 'twitter-user-name'
MENUITEMS = (('Blog', SITEURL),)
```

This flag will tell pelican to look in the /content/pages directory and display any .md or .rst document as a menu link. 
I'll use this for an 'about' page.
```
DISPLAY_PAGES_ON_MENU = True
```

```
cd content
mkdir pages
cd pages
touch about.md
```

Open the about page in your editor of choice.

Below are metadata that Pelican needs for content. See more [Pelican Metadata](https://docs.getpelican.com/en/latest/content.html#file-metadata)
```
Title: Title
Date: 2021-02-19 11:00
Category: Python
Tags: pelican, publishing, github, markdown
Slug: hello-world
Authors: Ethan King
Summary: Hello World
```

When you're ready to view current changes, test the website locally by running the dev server.
```bash
make devserver
```
navigate to http://localhost:8000/

## Setup Github Pages

To serve a static site on github, go to your repo and click on settings. Under the main 'options' tab, scroll down 
to the github pages settings and select the branch that will host the site. In this case , 'Main'.

![github pages settings]({static}/images/ghp_settings.png "github pages settings")

## setup using publishconf.py
publishconf.py
```python
SITEURL = 'http://your-domain-address'

FEED_ALL_ATOM = 'feeds/all.atom.xml'
CATEGORY_FEED_ATOM = 'feeds/%s.atom.xml'

MENUITEMS = (('Blog', SITEURL),)

DISQUS_SITENAME = ""
GOOGLE_ANALYTICS = ""
```

Push changes to the main branch and to the github remote repo.
```bash
make github
```
And the website is live! 
https://ethan-king.github.io/

