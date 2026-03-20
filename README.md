# 🐍 Python Selenium Training

A structured, hands-on training repository for learning **Selenium WebDriver with Python** — from project setup to advanced element interaction techniques.

---

## 📚 Table of Contents

- [Overview](#overview)
- [Prerequisites](#prerequisites)
- [Project Setup](#project-setup)
- [Sessions](#sessions)
  - [Session 1: Introduction to Selenium WebDriver](#session-1-introduction-to-selenium-webdriver)
  - [Session 2: Web Element Locators](#session-2-web-element-locators)
  - [Session 3: XPath in Selenium](#session-3-xpath-in-selenium)
- [Project Structure](#project-structure)
- [Resources](#resources)

---

## Overview

This repository contains code and examples written to support a **Python Selenium WebDriver training series**. Each session builds on the previous one, providing practical, runnable examples alongside conceptual explanations.

---

## Prerequisites

Before getting started, make sure you have the following installed:

- Python 3.8+
- pip (Python package manager)
- [PyCharm IDE](https://www.jetbrains.com/pycharm/) (recommended)
- Google Chrome or Firefox browser

Install dependencies:

```bash
pip install selenium
```

> **Note:** Selenium 4+ includes built-in browser driver management, so a separate ChromeDriver installation is not required.

---

## Project Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com/evaosorio15/Python-Selenium-Training.git
   cd Python-Selenium-Training
   ```

2. **Open in PyCharm** and configure your Python interpreter.

3. **Install dependencies** (see above).

4. **Run any session script** directly or via PyCharm's run configuration.

---

## Sessions

### Session 1: Introduction to Selenium WebDriver

**Topics Covered:**
- Setting up a Selenium project in PyCharm
- Writing your first basic test case
- Understanding WebDriver's architecture
- Key differences between **Selenium 3** and **Selenium 4**

**Key Concepts:**
| Topic | Description |
|---|---|
| WebDriver Architecture | How Selenium communicates with browsers via the W3C WebDriver protocol |
| Selenium 3 vs 4 | Selenium 4 uses W3C standard natively; no more JSON Wire Protocol |
| Basic Test Case | Open a browser, navigate to a URL, and close the session |

---

### Session 2: Web Element Locators

**Topics Covered:**
- Using built-in locators: `By.ID`, `By.NAME`
- Writing **CSS selectors** for flexible element targeting
- Practical examples using `find_element()` and `find_elements()`

**Locator Strategies Covered:**

| Locator | Example |
|---|---|
| `By.ID` | `driver.find_element(By.ID, "username")` |
| `By.NAME` | `driver.find_element(By.NAME, "email")` |
| `By.CSS_SELECTOR` | `driver.find_element(By.CSS_SELECTOR, "input.login-field")` |
| `By.XPATH` | `driver.find_element(By.XPATH, "//button[@type='submit']")` |
| `By.CLASS_NAME` | `driver.find_element(By.CLASS_NAME, "btn-primary")` |

### Session 3: XPath in Selenium

**Topics Covered:**
- Understanding **absolute vs. relative XPath**
- Writing XPath expressions using various attributes and operators
- Using browser tools for automated XPath generation

**XPath Types:**

| Type | Description | Example |
|---|---|---|
| Absolute XPath | Full path from root node — brittle, not recommended | `/html/body/div/form/input` |
| Relative XPath | Starts from any node in the DOM — flexible and preferred | `//input[@id='username']` |

**Common XPath Operators & Syntax:**

| Syntax | Purpose | Example |
|---|---|---|
| `@attribute` | Target by attribute | `//input[@type='text']` |
| `text()` | Target by visible text | `//button[text()='Login']` |
| `contains()` | Partial attribute/text match | `//div[contains(@class,'nav')]` |
| `and` / `or` | Combine conditions | `//input[@type='text' and @name='user']` |

**Tools for Automated XPath Generation:**
- Browser DevTools (right-click element → Copy → Copy XPath)
- Chrome extensions like **ChroPath** or **SelectorsHub**

---

## Project Structure

```
Python-Selenium-Training/
│
├── session_1/
│   └── intro_webdriver.py       # Basic WebDriver setup and first test
│
├── session_2/
│   └── element_locators.py      # Examples of various locator strategies
│
├── session_3/
│   └── xpath_locators.py        # Absolute vs. relative XPath examples
│
└── README.md
```

---

## Resources

- [Selenium Official Documentation](https://www.selenium.dev/documentation/)
- [Selenium Python Bindings](https://selenium-python.readthedocs.io/)
- [W3C WebDriver Specification](https://w3c.github.io/webdriver/)
- [PyCharm Download](https://www.jetbrains.com/pycharm/download/)

---

*Happy testing! 🚀*
