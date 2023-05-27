# PDF_app

Image to PDF converter and PDF merger in Python

Can run using the python script automation script from my [automations repo](https://www.github.com/adelin-diac/automations) (Will have exact link eventually).

To be able to run it using the automation script, please ensure that you have the following installed:

## Requirements

- Python 3.6+
- pip
- virtualenv (optional - if not used then packages will be installed globally)
- TkDND [install from here](https://github.com/petasis/tkdnd/releases)
- TKinterDnD2 [install from here](https://sourceforge.net/projects/tkinterdnd/files/)

## Installing the additional packages (TkDND and TKinterDnD2)

### TkDND

1. If using a 64-bit Windows machine, the `tkdnd2.9.2` version can be found in the `extra_packages` folder in this repo [tkdnd2.9.2](./extra_packages/tkdnd2.9.2/).

2. If using a different machine, the neccesary version can be found on github [here](https://github.com/petasis/tkdnd/releases).

3. Once you have installed and unzipped the folder, it must be added to the `tcl` directory in your Python installation. On Windows, this can noramlly be found in `C:\Users\{username}\AppData\Local\Programs\Python\Python{version}\tcl`. Just copy the `tkdnd2.9.2` (or whatever version you isntalled) folder into the `tcl` folder.

### TKinterDnD2

This is a wrapper package to the one we just installed. This can be downloaded from sourceforge [here](https://sourceforge.net/projects/tkinterdnd/files/), or it can be found in the `extra_packages` folder in this repo [here](./extra_packages/TkinterDnD2/).

Once downloaded and unzipped, you have two options:

1. You can add it to your `site-packages` folder in your Python installation. On Windows, this can normally be found in `C:\Users\{username}\AppData\Local\Programs\Python\Python{version}\Lib\site-packages`. Just copy the `TkinterDnD2` folder into the `site-packages` folder.

**OR**

2. You can add it into the `site-packages` folder in your virtual environment. Just copy the `TkinterDnD2` folder into the `venv\Lib\site-packages` folder. To create the virtualenvironment in this repo, you can do the following:

```bash
virtualenv venv
```

Then activate the virtual environment:

```bash
venv\Scripts\activate
```

Then install the packages:

```bash
pip install -r requirements.txt
```

Finally, drag the TkinerDnD2 folder into the `venv\Lib\site-packages` folder.

## Running the script

Once you have installed the packages, you can run the script using the following command:

```bash
python main.py
```
