### Installing Python

If you follow the instructions properly, you will find `python2`, `pip2`, `python3`, and `pip3` in your path. `python` by default will refer to `python2`.

#### Mac

##### Option 1 (Easiest)

Installing just the latest version of python 2 and 3 using Homebrew

```
brew install python python3
pip3 install virtualenvwrapper
```

##### Option 2 (Advanced)

Installing multiple versions of python using pyenv.

```
brew install pyenv
brew install pyenv-virtualenvwrapper
pyenv install 2.7.13 3.6.0
pyenv global 2.7.13 3.6.0
```

Add the following to your shell profile.
```
eval "$(pyenv init -)" && pyenv virtualenvwrapper
```

You will find `python2`, `pip2`, `python3`, and `pip3` in your path. `python` by default will refer to `python2`.

#### Ubuntu

##### Option 1 (Easiest)

Ubuntu 16.04 ships with both Python 3 and Python 2 pre-installed.

```
sudo apt-get update
sudo apt-get install -y python3-pip
```

#### Windows

https://www.python.org/downloads/windows/

```
¯\_(ツ)_/¯
```
