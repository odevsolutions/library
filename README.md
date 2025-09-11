[![Tech Doc](https://img.shields.io/badge/master-docs-875A7B.svg?style=flat&colorA=8F8F8F)](https://www.odoo.com/documentation/17.0)
[![Help](https://img.shields.io/badge/master-help-875A7B.svg?style=flat&colorA=8F8F8F)](https://www.odoo.com/forum/help-1)

# OdevS Development Assessment: Library Management System

This project serves as a pre-assessment for future applicants of [Odev Solutions](https://www.odevsolutions.com/). If you want to know more about the opportunities, please visit [https://www.odevsolutions.com/jobs](https://www.odevsolutions.com/jobs).

## Prerequisites

### Python and Odoo

We expect applicants to have a foundational understanding of Odoo and Python. If you are new to Odoo (trust us, it's amazing), please check out the [official website](https://odoo.com) and the [official developer documentation](https://www.odoo.com/documentation/master/developer.html).

### Git

Basic Git knowledge is required. Here are some resources to help you get started: [freeCodeCamp: The beginner’s guide to Git & GitHub](https://www.freecodecamp.org/news/the-beginners-guide-to-git-github/), [Git Immersion](https://gitimmersion.com/).

### Codespaces

This repository is set up to be opened in [Github Codspaces](https://github.com/features/codespaces), allowing you to easily start the exam without making any changes to your local machine.
Codespaces includes a [free tier](https://docs.github.com/en/billing/concepts/product-billing/github-codespaces#free-and-billed-use-by-personal-accounts) for personal accounts, with a limit of 120 core hours per month. Please note that OdevSolutions Co. will not cover any costs incurred from using Codespaces.

If you prefer a different kind of setup for your development environment, you are free to use it.

## Assessment Overview

This assessment involves creating a custom Odoo module for a simple library management system. An existing module in this repository can be used as a starting point. Refer to: [library](/addons_library/library).

## Getting Started

First, [fork](https://github.com/mikhail-trunks-silao/exam-library/fork) this repository and open it in Github Codespaces. Add your created module in `/addons_library` folder.

Refer to the sample snippet below for quick setup:

```bash
# Build the containers
docker-compose up -d
```

Refer below on how to stop, restart and remove containers.

```bash
# Stop and remove the containers
docker-compose down -d

# Restart the containers
docker restart exam-library-web-1 exam-library-db-1

# Stop the containers
docker stop exam-library-web-1 exam-library-db-1
```

If the port `8069` is not automatically forwarded from the Codespace to you local machine you 
can refer to the tutorial below on how to add it manually. <br/>
[Github: Forwarding ports in your codespace](https://docs.github.com/en/codespaces/developing-in-a-codespace/forwarding-ports-in-your-codespace?tool=vscode#forwarding-a-port-1)


## Tasks

### Task 1: Create a new Odoo module

Create a new module named `library_extensions`. It should depend on the `library` module.

This is where you will add your code for the other tasks.

### Task 2: Add an author field to the book model

Inherit the `library.book` model and add an `author_id` field.

- The `author_id` field should be a `Many2one` field with the `res.partner` model.
- The `author_id` field should be required.

### Task 3: Create a book category model

1. Create a new model named `library.book.category`. It should have a `name` field.

   - The `name` field should be a `Char` field.
   - The `name` field should be required.
   - The `name` field should be unique.

2. Add a `category_id` field to the `library.book` model. It should be a `Many2many` field with the `library.book.category` model.

3. A list and form view should also be created for the `library.book.category` model. The view should be accessible from the `Library > Book Category` menu. (You have to create a new menu item for this)

### Task 4: Updating the book model views

1. Update the `library.book` list view to display the following fields:

   - `author_id`
   - `category_id`

2. Update the `library.book` form view to display the following fields:

   - `author_id`
   - `category_id`

## What's next?

Now that you have completed the pre-assessment, you can continue to the [Odev Solutions](https://www.odevsolutions.com/) website and submit your application. Make sure your repository is public.

We will quickly review your submission and reach out to you for the next steps.

If you have any questions, contact us at [admin@odevsolutions.com](mailto:admin@odevsolutions.com).
