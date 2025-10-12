# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

# import sphinx_rtd_theme
# html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]

# import recommonmark

project = 'Feng Chi'
copyright = '2025, Feng Chi'
author = 'Feng Chi'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration



templates_path = ['_templates']
exclude_patterns = []

# language = 'en'

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

# html_theme = 'sphinx_rtd_theme'
# html_theme = 'press'
# html_static_path = ['_static']

html_theme ='sphinx_rtd_theme'
html_static_path = ['_static']
html_logo = 'trident-large.png' 
html_theme_options = {
    'logo_only': False,
    'display_version': False,
}

# extensions = ['recommonmark']

# from recommonmark.parser import CommonMarkParser
# source_parsers = {
#    '.md': CommonMarkParser,
#}
# source_suffix = ['.rst', '.md']


html_static_path = ['_static']

# 注册自定义 CSS
def setup(app):
    app.add_css_file('mycss.css')  # 加载创建的CSS文件



extensions = [
    # ... 数学公式扩展项
    'sphinx.ext.mathjax',  # 推荐，使用MathJax渲染
    # 或 'sphinx.ext.imgmath' （生成图片格式公式）
]

extensions = ['myst_parser']
source_suffix = {
    '.rst': 'restructuredtext',
    '.md': 'markdown',
}

myst_enable_extensions = [
    "amsmath",
    "attrs_inline",
    "colon_fence",
    "deflist",
    "dollarmath",
    "fieldlist",
    "html_admonition",
    "html_image",
    "linkify",
    "replacements",
    "smartquotes",
    "strikethrough",
    "substitution",
    "tasklist",
]




