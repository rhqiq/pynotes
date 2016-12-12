# Deep Learning Workshop

## Setup

This course assumes that you are using a Python environment with the necessary dependencies. If you are comfortable with managing Python environments, you can install these dependencies directly with `pip` in your environment. If you prefer, you can use the Anaconda environment, which comes with these tools already. Instructions for both options are below.

### Python environment setup

To install dependencies in your Python environment:
```
pip install Jupyter
pip install sklearn
pip install matplotlib
```

### Anaconda

You can download Anaconda python by running the following and going through the prompts:

```
curl -O https://repo.continuum.io/archive/Anaconda2-4.2.0-MacOSX-x86_64.sh
bash Anaconda2-4.2.0-MacOSX-x86_64.sh
```

The installation script will optionally prepend the Anaconda `bin` directory to your path in your `.bash_profile`. Before continuting, be sure that Anaconda is on your path by running `which python` and confirming it is the Anaconda version. You may need to source your `.bash_profile` (or open a new terminal).


### Installing Tensorflow

After your environment is setup, you should be able to install Tensorflow. If you are using a Mac, you can install Tensorflow 0.12, the latest release, with

```
pip install https://storage.googleapis.com/tensorflow/mac/cpu/tensorflow-0.12.0rc0-py2-none-any.whl
```

If you are running on a different OS, find the correct version for you from the [various available builds](https://www.tensorflow.org/versions/r0.12/get_started/os_setup.html#using-pip).

You can test that all is well with your installation by running `ipython` and then executing `import tensorflow`. If this runs without errors, your environment is setup.