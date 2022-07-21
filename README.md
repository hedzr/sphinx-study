# sphinx study


[![Documentation Status](https://readthedocs.org/projects/hz-sphinx-study/badge/?version=latest)](https://hz-sphinx-study.readthedocs.io/en/latest/?badge=latest)


a notebook for studying sphinx documenter.

This repo is a expeiremental notebook for studying how to use sphinx to build a online docsite.

[status admin](https://readthedocs.org/projects/hz-sphinx-study/)


## Build

The following command will install the packages according to the configuration file requirements.txt.

install

```bash
pip install -r requirements.txt
```

freeze

```bash
pip freeze > requirements.txt
```

list

```bash
pip list
```


## How to Create Python Requirements File After Development

While it is possible to create it manually, it is a good practice to use the pipreqs module. It is used to scan your imports and build a Python requirements file for you.

According to [THE DOCUMENTATION](https://github.com/bndr/pipreqs), once installed with the following command:

```bash
pip install pipreqs
```

running pipreqs in the command line generates a `requirements.txt` file automatically:

```bash
$ pipreqs /home/project/location
Successfully saved requirements file in   /home/project/location/requirements.txt
```
