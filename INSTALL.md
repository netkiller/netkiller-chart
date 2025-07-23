# Install

## requirements

```shell
brew install cairo libsvg-cairo pkg-config
```

```shell
pip install --upgrade pip
# pip install -r requirements.txt
# pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple
# PS D:\workspace\netkiller> .\.venv\Scripts\pip.exe install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple
```

## setuptools

```shell
    $ pip install setuptools wheel twine
	$ cd /usr/local/src/
	$ git clone https://github.com/netkiller/netkiller-chart.git
	$ cd netkiller-chart
	$ python3 setup.py sdist
	$ python3 setup.py install --prefix=/srv/netkiller-chart
```

## RPM 包

```shell
    $ python setup.py bdist_rpm

```

## Windows 文件

```shell
    $ python setup.py bdist_wininst
```

## Deploy Pypi

```shell
	$ pip install setuptools wheel twine
	$ python setup.py sdist bdist_wheel
	$ twine upload dist/netkiller-chart-x.x.x.tar.gz 

```

## pyproject.toml

```shell
pip install build -i https://pypi.tuna.tsinghua.edu.cn/simple
python -m build
pip install dist/netkiller-chart-0.0.1-py3-none-any.whl --force-reinstall

(.venv) neo@Neo-Mac-mini-M4 netkiller-chart % twine upload dist/netkiller-chart-0.0.1*

(.venv) neo@Neo-Mac-mini-M4 netkiller-chart % pip install netkiller-chart
```