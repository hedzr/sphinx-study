# 附加

## 文章的信息块

`article-info` 指令用于显示有关文章的信息块，通常位于文章标题的正下方（如下所示，带有非标准大纲）。

```{article-info}
:avatar: ../../../_static/logo-square.svg
:avatar-link: https://github.com/hedzr/
:avatar-outline: muted
:author: hedzr
:date: "2022-01-29"
:read-time: "5 min"
:class-container: sd-p-2 sd-outline-muted sd-rounded-1
```

````{tab-set-code}
```{literalinclude} ./snippets/myst/article-info.txt
:language: myst markdown
```
```{literalinclude} ./snippets/rst/article-info.txt
:language: rst
```
````

### 可选项

```{eval-rst}
.. include:: ./snippets/article-info-option.rst
```
