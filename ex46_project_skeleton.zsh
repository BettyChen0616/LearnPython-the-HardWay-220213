(base) % pip list
Package                            Version
---------------------------------- -------------------
pip                                20.2.4
setuptools                         50.3.1.post20201107

(base) % sudo pip install virtualenv
Successfully installed distlib-0.3.4 filelock-3.6.0 platformdirs-2.5.0 virtualenv-20.13.1


(base) % virtualenv --version
virtualenv 20.13.1 from /Users/jiayuchen/opt/anaconda3/lib/python3.8/site-packages/virtualenv/__init__.py


'creat a directory called .venvs in HOME ~/ to store all my virtual environments '
(base) % mkdir ~/.venvs

'run virtualenv and tell it to include the system site packages,
then instruct it to build the virtualenv in ~/. venvs/lpthw'
(base) % virtualenv --system-site-packages ~/.venvs/lpthw
created virtual environment CPython3.8.5.final.0-64 in 329ms
  creator CPython3Posix(dest=/Users/jiayuchen/.venvs/lpthw, clear=False, no_vcs_ignore=False, global=True)
  seeder FromAppData(download=False, pip=bundle, setuptools=bundle, wheel=bundle, via=copy, app_data_dir=/Users/jiayuchen/Library/Application Support/virtualenv)
    added seed packages: pip==22.0.3, setuptools==60.6.0, wheel==0.37.1
  activators BashActivator,CShellActivator,FishActivator,NushellActivator,PowerShellActivator,PythonActivator

'source the lpthw virtual environment by using the . operator in bash,
followed by the ~/.venvs/lpthw/bin/activate script'
(base) % . ~/.venvs/lpthw/bin/activate

(lpthw) (base) % which python
/Users/jiayuchen/.venvs/lpthw/bin/python
(lpthw) (base) % python
Python 3.8.5 (default, Sep  4 2020, 02:22:02)
[Clang 10.0.0 ] :: Anaconda, Inc. on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> quit()

(lpthw) (base) % pip install nose
Requirement already satisfied: nose in ./opt/anaconda3/lib/python3.8/site-packages (1.3.7)

(lpthw) (base) % mkdir projects
(lpthw) (base) % cd projects
(lpthw) (base) % mkdir skeleton
(lpthw) (base) % cd skeleton
(lpthw) (base) % mkdir bin NAME tests docs
(lpthw) (base) % touch NAME/__init__.py
(lpthw) (base) % touch tests/__init__.py

'创建setup.py 文件和 NAME_tests.py 文件'
(lpthw) (base) % cd skeleton
(lpthw) (base) % ls -R
NAME		bin		docs		setup.py	tests

./NAME:
__init__.py

./bin:

./docs:

./tests:
NAME_tests.py	__init__.py

'在此级目录中运行nosetests，测试setup'
(lpthw) (base) % nosetests
.
----------------------------------------------------------------------
Ran 1 test in 0.004s

OK
