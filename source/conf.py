# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))

#

import sys
import os
import shlex

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
sys.path.insert(0, os.path.abspath('../src'))
# sys.path.insert(0, os.path.abspath('../../..'))
# sys.path.insert(0, os.path.abspath('.'))

# import recommonmark
# from recommonmark.transform import AutoStructify
# from recommonmark.parser import CommonMarkParser;

from datetime import date

from sphinx.application import Sphinx
from myst_nb import __version__ as myst_nb_version

source_suffix = ['.rst', '.md', '.MD', '.ipynb', '.myst']
source_suffix = {
    '.rst': 'restructuredtext',
    '.ipynb': 'myst-nb',
    '.myst': 'myst-nb',
    '.md': 'myst-nb',
}

# -- Project information -----------------------------------------------------

project = 'HZNB'
copyright = '2022, hedzr'
author = 'hedzr'

# The short X.Y version
version = '0.1.1'

# The full version, including alpha/beta/rc tags
release = '0.1.1'

brief = u'cmdr-cxx is a POSIX-compliant command-line arguments parser in C++, its part of cmdr series.'

github_url = 'https://github.com/hedzr/cmdr-cxx'
github_doc_root = 'https://github.com/hedzr/cmdr-cxx/tree/master/docs/manual/'

# The master toctree document.
master_doc = 'index'
language = "en"
# language = 'zh_CN'

# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.doctest',
    'sphinx.ext.intersphinx',
    'sphinx.ext.todo',
    'sphinx.ext.coverage',
    'sphinx.ext.imgmath',
    'sphinx.ext.mathjax',
    'sphinx.ext.ifconfig',
    'sphinx.ext.viewcode',
    'sphinx.ext.githubpages',

    # "myst_parser",
    "myst_nb",
    "sphinx_design",  # 用于设计美观、视图大小的响应式 Web 组件。
    'sphinx_tabs.tabs',
    "sphinxext.rediraffe",
    "sphinxcontrib.mermaid",  # 美人鱼，通过代码生成时序图等
    "sphinxext.opengraph",
    "sphinx.ext.autosectionlabel",  # Auto-generate section labels. label 标签自动选中确保唯一性,并允许引用节使用其标题,同时自动为标题创建label
    #
    # 'sphinx.ext.napoleon',
    # 'recommonmark',
    #
    "sphinx_thebe",  # 使您的代码单元与Thebe和Binder提供的内核进行交互。
    #
    "sphinx_copybutton",  # 代码块复制按钮扩展
    "sphinx_togglebutton",  # 折叠警告（注释、警告等）的功能按钮
    # 评论区
    # "sphinx_comments",
    'breathe',
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = 'en'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
# exclude_patterns = []
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

# The encoding of source files.
#source_encoding = 'utf-8-sig'

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'alabaster'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']
html_css_files = ["custom.css"]

html_theme = "sphinx_book_theme"
html_logo = "_static/logo-wide.svg"
html_favicon = "_static/logo-square.svg"
# html_logo = "_static/notebook-badge.svg"
# html_favicon = "_static/logo-square.svg"
# html_title = ""
html_theme_options = {
    "home_page_in_toc": True,
    "github_url": github_url,
    "repository_url": github_url,
    "repository_branch": "master",
    "path_to_docs": ".",
    "use_repository_button": True,
    "use_edit_page_button": True,

    # （仅限开发人员）触发一些功能，使开发主题更容易。默认 `False`
    # "theme_dev_mode": False,

    # ----------------主题内容中导航栏的功能按钮配置--------
    # 添加存储库链接
    # "repository_url": "https://github.com/Eugene-Forest/NoteBook",
    # 添加按钮以链接到存储库
    # "use_repository_button": True,
    # 要添加按钮以打开有关当前页面的问题
    "use_issues_button": True,
    # 添加一个按钮来建议编辑
    # "use_edit_page_button": True,
    # 在导航栏添加一个按钮来切换全屏的模式。
    "use_fullscreen_button": True,  # 默认 `True`
    # 默认情况下，编辑按钮将指向master分支，但如果您想更改此设置，请使用以下配置
    # "repository_branch": "main",
    # 默认情况下，编辑按钮将指向存储库的根目录；而我们 sphinx项目的 doc文件其实是在 source 文件夹下的，包括 conf.py 和 index(.rst) 主目录
    # "path_to_docs": "source",
    # 您可以添加 use_download_button 按钮，允许用户以多种格式下载当前查看的页面
    # "use_download_button": False,

    # --------------------------右侧辅助栏配置---------
    # 重命名右侧边栏页内目录名，标题的默认值为Contents。
    # "toc_title": "导航",
    # -- 在导航栏中显示子目录，向下到这里列出的深度。 ----
    "show_toc_level": 2,
    # --------------------------左侧边栏配置--------------
    # -- 只显示标识，不显示 `html_title`，如果它存在的话。-----
    "logo_only": True,
    # 控制左侧边栏列表的深度展开,默认值为1，它仅显示文档的顶级部分
    "show_navbar_depth": 1,
    # 自定义侧边栏页脚,默认为 Theme by the Executable Book Project
    # "extra_navbar": "<p>Your HTML</p>",
    # "home_page_in_toc": False,  # 是否将主页放在导航栏（顶部）
    # ------------------------- 单页模式 -----------------
    # 如果您的文档只有一个页面，并且您不需要左侧导航栏，那么您可以 使用以下配置将其配置sphinx-book-theme 为以单页模式运行
    # "single_page": True,

    # 用于交互的启动按钮
    # Thebe将您的静态代码块转换 为由 Jupyter 内核提供支持的交互式代码块。它通过要求一个BinderHub内核做到这一点 的引擎盖下，您的所有代码细胞转换成互动码单元。这允许用户在不离开页面的情况下在您的页面上运行代码。
    # "launch_buttons": {
    #     "binderhub_url": "https://mybinder.org",
    #     # 控制打开的用户界面
    #     "notebook_interface": "jupyterlab",
    #     "thebe": True,
    # },
    # -- 在每个页面的页脚添加额外的 HTML。---
    # "extra_footer": '',
}
# OpenGraph metadata
ogp_site_url = "https://cmdr-cxx.readthedocs.io/en/latest"
# This is the image that GitHub stores for our social media previews
ogp_image = "https://repository-images.githubusercontent.com/240151150/316bc480-cc23-11eb-96fc-4ab2f981a65d"  # noqa: E501
ogp_custom_meta_tags = [
    '<meta name="twitter:card" content="summary_large_image">',
]

# If not '', a 'Last updated on:' timestamp is inserted at every page bottom,
# using the given strftime format.
html_last_updated_fmt = '%b %d, %Y'

# If true, SmartyPants will be used to convert quotes and dashes to
# typographically correct entities.
#html_use_smartypants = True

# Custom sidebar templates, maps document names to template names.
# 通过html文件定制主侧栏
#html_sidebars = {}

# Additional templates that should be rendered to pages, maps page names to
# template names.
#html_additional_pages = {}

# If false, no module index is generated.
#html_domain_indices = True

# If false, no index is generated.
#html_use_index = True

# If true, the index is split into individual pages for each letter.
#html_split_index = False

# If true, links to the reST sources are added to the pages.
#html_show_sourcelink = True

# If true, "Created using Sphinx" is shown in the HTML footer. Default is True.
#html_show_sphinx = True

# If true, "(C) Copyright ..." is shown in the HTML footer. Default is True.
#html_show_copyright = True

# If true, an OpenSearch description file will be output, and all pages will
# contain a <link> tag referring to it.  The value of this option must be the
# base URL from which the finished HTML is served.
#html_use_opensearch = ''

# This is the file name suffix for HTML files (e.g. ".xhtml").
#html_file_suffix = None

# Output file base name for HTML help builder.
# htmlhelp_basename = 'NoteBookdoc'

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
# language = "en"

# # The reST default role (used for this markup: `text`) to use for all
# # documents.
# default_role = None

# # The name of the Pygments (syntax highlighting) style to use.
# pygments_style = 'sphinx'

# -- Extension configuration -------------------------------------------------

# -- Options for intersphinx extension ---------------------------------------

# Example configuration for intersphinx: refer to the Python standard library.
intersphinx_mapping = {
    # 'python': ('https://docs.python.org/3', None),
    "python": ("https://docs.python.org/3.7", None),
    "sphinx": ("https://www.sphinx-doc.org/en/master", None),
    "markdown_it": ("https://markdown-it-py.readthedocs.io/en/latest", None),
}

# -- Options for todo extension ----------------------------------------------

# If true, `todo` and `todoList` produce output, else they produce nothing.
todo_include_todos = True

# Prefix document path to section labels, otherwise autogenerated labels would look like 'heading'
# rather than 'path/to/file:heading'
autosectionlabel_prefix_document = True

# 控制切换按钮悬停文本
# togglebutton_hint = "展示隐藏内容"

thebe_config = {
    "repository_url": github_url,
    "repository_branch": "master",
}

# -- Options for MyST output -------------------------------------------------

myst_enable_extensions = [
    "amsmath",
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
myst_number_code_blocks = ["typescript"]
myst_heading_anchors = 2
# 在 myst 0.17.0 （0.16.1） 版本中才有语法删除线 "strikethrough",
# 禁止显示myst.strikethrough警告
suppress_warnings = ["myst.strikethrough"]

# 如果为false,只有包含方案（例如http）的链接才会被识别为外部链接
myst_linkify_fuzzy_links = False
# myst_footnote_transition = True

# 数学公式语法 $ （dollar math） 设置
myst_dmath_allow_labels = True
myst_dmath_double_inline = True
# myst_dmath_allow_space = False, will cause inline math to only be parsed if there are no initial / final spaces, e.g. $a$ but not $ a$ or $a $.
# myst_dmath_allow_digits = False, will cause inline math to only be parsed if there are no initial / final digits, e.g. $a$ but not 1$a$ or $a$2.

# substitution 的扩展的全局替换，作用于 .md
myst_substitutions = {
    "sphinx": "4.3.2",
    "sphinx_autobuild": "2021.3.14",
    "sphinx_book_theme": "0.1.7",
    "myst_parser": "0.15.2",
    "myst_nb_version": myst_nb_version,
    "markdown": "3.3.4",
    "markdown_it_py": "1.1.0",
    "sphinx_tabs": "3.2.0",
    "sphinx_thebe": "0.0.10",
    "sphinx_togglebutton": "0.2.3",
    "sphinx_design": "0.0.13",
    "sphinx_copybutton": "0.4.0",
}
# default is ['{', '}']，替换指令分隔符，不建议更改
# myst_sub_delimiters = ["|", "|"]

# 评论区扩展功能配置样例
# comments_config = {
#     "hypothesis": True,
#     "dokieli": False,
#     "utterances": {
#         "repo": "xinetzone/sphinx-demo",
#         "optional": "config",
#     }
# }

# rediraffe_redirects = {
#     "using/intro.md": "sphinx/intro.md",
#     "sphinx/intro.md": "intro.md",
#     "using/use_api.md": "api/index.md",
#     "api/index.md": "api/reference.rst",
#     "using/syntax.md": "syntax/syntax.md",
#     "using/syntax-optional.md": "syntax/optional.md",
#     "using/reference.md": "syntax/reference.md",
#     "sphinx/reference.md": "configuration.md",
#     "sphinx/index.md": "faq/index.md",
#     "sphinx/use.md": "faq/index.md",
#     "sphinx/faq.md": "faq/index.md",
#     "explain/index.md": "develop/background.md",
# }

# -- Options for Breathe/Doxygen output -------------------------------------------------

import subprocess, os


def configureDoxyfile(base_dir, proj_dir, input_dir, output_dir):
    f = base_dir + '/Doxyfile.in'
    if os.path.isfile(f):
        with open(f, 'r') as file:
            filedata = file.read()

            filedata = filedata.replace('@DOXYGEN_INPUT_DIR@', input_dir)
            filedata = filedata.replace('@DOXYGEN_OUTPUT_DIR@', output_dir)

            filedata = filedata.replace('@PROJECT_NAME@', project)
            filedata = filedata.replace('@PROJECT_VERSION@', version)
            filedata = filedata.replace('@PROJECT_BRIEF@', brief)
            filedata = filedata.replace('@PROJECT_LOGO@', 'logo-wide.svg')
            filedata = filedata.replace('@CMAKE_CURRENT_SOURCE_DIR@', '..')
            filedata = filedata.replace('@PROJECT_SOURCE_DIR@', '../..')
            filedata = filedata.replace('@CMAKE_CURRENT_SOURCE_DIR_LINUX@',
                                        '..')

            with open(proj_dir + '/Doxyfile', 'w') as file:
                file.write(filedata)
            return True
    return False


# Check if we're running on Read the Docs' servers
read_the_docs_build = os.environ.get('READTHEDOCS', None) == 'True'
# read_the_docs_build = True
breathe_projects = {}

if read_the_docs_build:
    base_dir = '../..'
    proj_dir = base_dir + '/doxygen'
    input_dir = '..'
    output_dir = input_dir + '/build'
    if configureDoxyfile(base_dir, proj_dir, input_dir, output_dir):
        subprocess.call('doxygen', cwd=proj_dir, shell=True)
        breathe_projects[project] = '../' + output_dir + '/xml'
        breathe_default_project = project
else:
    dir = '../../build/xml'
    if os.path.isdir(dir) and os.path.isfile(dir + '/namespacecmdr.xml'):
        breathe_projects[project] = dir
        breathe_default_project = project

#
# -- Options for More output ---------------------------------------------

# autodoc_default_options = {
#     "show-inheritance": True,
#     "special-members": "__init__, __enter__, __exit__",
#     "members": True,
#     # 'exclude-members': '',
#     "undoc-members": True,
#     # 'inherited-members': True
# }
autodoc_member_order = "bysource"
nitpicky = True
nitpick_ignore = [
    ("py:class", "docutils.nodes.document"),
    ("py:class", "docutils.nodes.docinfo"),
    ("py:class", "docutils.nodes.Element"),
    ("py:class", "docutils.nodes.Node"),
    ("py:class", "docutils.nodes.field_list"),
    ("py:class", "docutils.nodes.problematic"),
    ("py:class", "docutils.nodes.pending"),
    ("py:class", "docutils.nodes.system_message"),
    ("py:class", "docutils.statemachine.StringList"),
    ("py:class", "docutils.parsers.rst.directives.misc.Include"),
    ("py:class", "docutils.parsers.rst.Parser"),
    ("py:class", "docutils.utils.Reporter"),
    ("py:class", "nodes.Element"),
    ("py:class", "nodes.Node"),
    ("py:class", "nodes.system_message"),
    ("py:class", "Directive"),
    ("py:class", "Include"),
    ("py:class", "StringList"),
    ("py:class", "DocutilsRenderer"),
    ("py:class", "MockStateMachine"),
]

# -- Options for LaTeX output ---------------------------------------------

latex_elements = {
    # The paper size ('letterpaper' or 'a4paper').
    #'papersize': 'letterpaper',

    # The font size ('10pt', '11pt' or '12pt').
    #'pointsize': '10pt',

    # Additional stuff for the LaTeX preamble.
    #'preamble': '',

    # Latex figure (float) alignment
    #'figure_align': 'htbp',
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [
    (master_doc, 'cmdr-cxx.tex', u'cmdr-cxx Documentation',
     u'hedzr, and contributors', 'manual'),
]

# The name of an image file (relative to this directory) to place at the top of
# the title page.
#latex_logo = None

# For "manual" documents, if this is true, then toplevel headings are parts,
# not chapters.
#latex_use_parts = False

# If true, show page references after internal links.
#latex_show_pagerefs = False

# If true, show URL addresses after external links.
#latex_show_urls = False

# Documents to append as an appendix to all manuals.
#latex_appendices = []

# If false, no module index is generated.
#latex_domain_indices = True

# -- Options for manual page output ---------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [(master_doc, 'cmdr-cxx', u'cmdr-cxx Documentation', [author], 1)]

# If true, show URL addresses after external links.
#man_show_urls = False

# -- Options for Texinfo output -------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
    (master_doc, 'cmdr-cxx', u'cmdr-cxx Documentation', author, 'cmdr-cxx',
     'One line description of project.', 'Miscellaneous'),
]

# Documents to append as an appendix to all manuals.
#texinfo_appendices = []

# If false, no module index is generated.
#texinfo_domain_indices = True

# How to display URL addresses: 'footnote', 'no', or 'inline'.
#texinfo_show_urls = 'footnote'

# If true, do not generate a @detailmenu in the "Top" node's menu.
#texinfo_no_detailmenu = False

# -- Options for Epub output -------------------------------------------------

# Bibliographic Dublin Core info.
epub_title = project

# The unique identifier of the text. This can be a ISBN number
# or the project homepage.
#
# epub_identifier = ''

# A unique identification for the text.
#
# epub_uid = ''

# A list of files that should not be packed into the epub file.
epub_exclude_files = ['search.html']

# -- global replace order configuration are as follows---
# 全局字符串替换指令
# 需要注意的是，全局加入替换的功能要谨慎使用，要酌情使用；因为在这里添加后会影响到项目所有的 rst 文件（在所有 rst 文件中添加定义的替换指令）
# 一串 reStructuredText，它将包含在每个读取的源文件的末尾。 这是一个可以添加应该在每个文件中可用的替换的地方
rst_prolog = """
.. |15| raw:: html
      
      <hr width='15%'>

.. |30| raw:: html
      
      <hr width='30%'>
      
.. |50| raw:: html
      
      <hr width='50%'>

.. |75| raw:: html
      
      <hr width='75%'>

.. |mysql| replace:: **MySQL**

.. |mssql| replace:: **SQL Server**

"""

# ".. |java| replace::  **Java**"
# ".. |centos| replace:: **CentOS 7.x**"
# ".. |idea| replace:: **IntelliJ IDEA**"

# 图片编号功能
# -- numfig configuration are as follows---
# 表格和代码块如果有标题则会自动编号
numfig = True
# -- numfig_secnum_depth configuration are as follows---
# 如果设置为“0”，则数字，表格和代码块从“1”开始连续编号。
# 如果“1”(默认)，数字将是“x.1”。“x.2”，… 与“x”的节号(顶级切片;没有“x”如果没有部分)。只有当通过 toctree 指令的“:numbered:”选项激活了段号时，这才自然适用。
# 如果“2”，表示数字将是“x.y.1”，“x.y.2”，…如果位于子区域(但仍然是 x.1 ，x.2 ，… 如果直接位于一个部分和 1 ，2 ， … 如果不在任何顶级部分。)
numfig_secnum_depth = 2
# -- numfig_format configuration are as follows---
# 一个字典将“‘figure’”，“‘table’”，“‘code-block’”和“‘section’”映射到用于图号格式的字符串。作为一个特殊字符，“%s”将被替换为图号。
# 默认是使用“‘Fig.%s’”为“‘figure’”, “‘Table%s’”为“‘table’”，“‘Listing%s’”为“‘code-block’”和“‘Section’”为 “‘section’”。
# numfig_format = {'code-block': '代码块 %s', }
# -- html_codeblock_linenos_style configuration are as follows---
# 代码块的行号样式
html_codeblock_linenos_style = 'table'

# html_codeblock_linenos_style = 'inline'


# app setup hook
def setup(app):
    # app.add_config_value('recommonmark_config', {
    #     #'url_resolver': lambda url: github_doc_root + url,
    #     'auto_toc_tree_section': 'Contents',
    #     'enable_math': False,
    #     'enable_inline_math': False,
    #     'enable_eval_rst': True,
    #     # 'enable_auto_doc_ref': True,
    # }, True)
    # app.add_transform(AutoStructify)

    # """Add functions to the Sphinx setup."""
    # from myst_parser._docs import (
    #     DirectiveDoc,
    #     DocutilsCliHelpDirective,
    #     MystConfigDirective,
    # )

    app.add_css_file("custom.css")
    # app.add_directive("myst-config", MystConfigDirective)
    # app.add_directive("docutils-cli-help", DocutilsCliHelpDirective)
    # app.add_directive("doc-directive", DirectiveDoc)
