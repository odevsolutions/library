[![Tech Doc](https://img.shields.io/badge/master-docs-875A7B.svg?style=flat&colorA=8F8F8F)](https://www.odoo.com/documentation/17.0)
[![Help](https://img.shields.io/badge/master-help-875A7B.svg?style=flat&colorA=8F8F8F)](https://www.odoo.com/forum/help-1)

# OdevS Development Assessment: Library Management System

This project serves as a pre-assessment for future applicants of [Odev Solutions](https://www.odevsolutions.com/). If you want to know more about the opportunities, please visit [https://www.odevsolutions.com/jobs](https://www.odevsolutions.com/jobs).

## Prerequisites

### Python and Odoo

We expect applicants to have a foundational understanding of Odoo and Python. If you are new to Odoo (trust us, it's amazing), please check out the [official website](https://odoo.com) and the [official developer documentation](https://www.odoo.com/documentation/master/developer.html).

### Git

Basic Git knowledge is required. Here are some resources to help you get started: [freeCodeCamp: The beginner’s guide to Git & GitHub](https://www.freecodecamp.org/news/the-beginners-guide-to-git-github/), [Git Immersion](https://gitimmersion.com/).

### Docker

We use Docker for our development environment. Ensure Docker is installed on your machine by following this guide: [Get Docker](https://docs.docker.com/get-docker/).

You should also be able to set up an Odoo container using the [odoo:17](https://hub.docker.com/_/odoo) image. Refer to the usage guide on the page for detailed instructions.

> Author's note: We should consider creating our own guide for this.

## Assessment Overview

This assessment involves creating a custom Odoo module for a simple library management system. An existing module in this repository can be used as a starting point. Refer to: [library](library).

## Getting Started

First, [fork](https://github.com/odevsolutions/library/fork) this repository and clone it to your local machine. Then add the repository in your Odoo instance's addons path.

Refer to the sample snippet below for quick setup:

```bash
git clone https://github.com/your-username/library.git
docker run -v library:/mnt/extra-addons \
     --name odoo \
     -p 8069:8069 \
     --link postgres:db \
     -t odoo:17
```

> Note: This snippet assumes that a postgres container is already running.

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
