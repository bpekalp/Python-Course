# Python Course

This repository contains all the source files of the projects I developed while following the [Python Mega Course](https://www.udemy.com/course/the-python-mega-course) by [Ardit Sulce](https://www.linkedin.com/in/arditsulce).

# Preparing The Environment

There are some libraries that you need to install in order to run the applications. Although you can install the libraries globally, the recommended way to install these libraries is by creating a virtual python environment first.

First, you have to clone the repo by running the following command:

```bash
git clone https://github.com/bpekalp/Python-Course.git
```

Then, navigate into the repo by running the following command:

```bash
cd Python-Course
```

Then, create a virtual environment by running the following command:

```bash
python -m venv .venv
```

Then, you'll need to activate the virtual environment that you've just created. Don't forget to activate the virtual environment every time before running the apps.

- On Windows, run the following command:

```shell
.venv\Scripts\activate
```

- On MacOS, run the following command:

```bash
source .venv/bin/activate
```

- On Linux:
  - Run the following command if you're using bash:

```bash
source .venv/bin/activate
```

- Or if you're using zsh

```bash
source .venv/bin/activate.zsh
```

- Or if you're using fish:

```bash
source .venv/bin/activate.fish
```

And finally, you can install the required libraries and run the applications. To install the libraries run the following command:

```bash
pip install -r requirements.txt
```

# Web Apps

You can find all the web apps I developed on [this website!](https://gbp-py-webapps.streamlit.app/)

## To-Do App

To-Do application comes with 3 variations:

- **CLI**
- **GUI**
- **Web App**

You can launch the CLI version by running the following command:

```bash
python cli.py
```

You can launch the GUI version by downloading the release or running the following command:

```bash
python gui.py
```

You can launch the Web version by visiting my [web apps site](https://gbp-py-webapps.streamlit.app/) or running the following command:

```bash
streamlit run web.py
```

## E-Portfolio App

The e-portfolio app is a web app that displays user projects. It comes with a fully functioning contact me page.

The data source is provided by [Ardit Sulce](https://www.linkedin.com/in/arditsulce) in [Python Mega Course](https://www.udemy.com/course/the-python-mega-course)

You can launch the web app by visiting my [web apps site](https://gbp-py-webapps.streamlit.app/) or running the following command:

```bash
streamlit run home.py
```

# Console Apps

## PDF Maker

The PDF maker application uses FPDF library. The app generates a PDF file in following format. In the app, the allocated number of pages is read from the `.csv` file for each section.

You can run the app by running the following command:

```bash
python main.py
```

### Title

---

(The generated files are empty so there is no content)

_Page Number, Title_

## Invoice Generator

The Invoice Generator application reads purchase data from `.xlsx` files and creates a generic invoice that includes a table with a grand total row.

You can run the app by running the following command:

```bash
python main.py
```
