Create your own python module for anything example calculator etc.
create wheel package of this module, install this module and test it, while installing wheel package it should also install its dependencies automatically 

# Overview
text_utils is a lightweight Python package designed for simple yet essential text processing operations. It allows users to analyze and manipulate text through 
functions like word counting, character counting, finding common words, and converting text to uppercase or lowercase. 

# Package Build and Distribution Process

When you run the command python3 setup.py sdist bdist_wheel for your text_utils package, it first generates a source distribution (.tar.gz) that includes all
your Python files and necessary resources. Then, it creates a wheel distribution (.whl), which is a pre-compiled version of the package that can be installed 
without needing to build it from source. These distributions are saved in the dist/ directory, and the .whl file can be easily installed using pip, ensuring 
fast and efficient installation across different systems. This process allows you to share your package with others in a convenient, ready-to-use format.

Installing the Package: Once the wheel file is generated, you can install the package on your local system using pip:
```bash
pip install dist/text_utils-0.1-py3-none-any.whl
```
# Snapshots:

![Screenshot from 2024-11-11 12-38-56](https://github.com/user-attachments/assets/7b28f042-9b23-4827-844e-fc616540e79f)
