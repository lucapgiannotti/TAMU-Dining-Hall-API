# TAMU Dining Halls Menu API

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

This API provides the food menu for Texas A&M University dining halls for breakfast, lunch, and dinner. It's designed to help students and staff easily access daily meal options.

## Table of Contents
- [Introduction](#introduction)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
  - [Endpoints](#endpoints)
  - [Example Requests](#example-requests)
- [Contributing](#contributing)
- [License](#license)

## Introduction
The TAMU Dining Halls Menu API allows users to retrieve the daily menu for various dining halls at Texas A&M University. It supports querying for breakfast, lunch, and dinner menus.

## Features
- Retrieve daily menus for breakfast, lunch, and dinner.
- Filter menus by specific dining halls. **(WIP)**
- Easy-to-use RESTful API endpoints.

## Installation
To run this API locally using Flask, follow these steps:

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/TAMU-Dining-Halls-Menu-API.git
   cd TAMU-Dining-Halls-Menu-API
   ```
2. **Create a virtual environment**
   ```bash
   python3 -m venv venv
   source venv/bin/activate   # On Windows use `venv\Scripts\activate`
   ```
3. **Install Depedencies**
   ```bash
   pip install -r requirements.txt```

## Usage
### Endpoints
| Method | Endpoint                                 | Description                                      |
|--------|------------------------------------------|--------------------------------------------------|
| GET    | /api/menus/breakfast_menu                | Retrieve breakfast menu                          |
| GET    | /api/menus/lunch_menu                    | Retrieve lunch menu                              |
| GET    | /api/menus/dinner_menu                   | Retrieve dinner menu                             |
| GET    | /api/menus/:diningHall/breakfast         | Retrieve breakfast menu for specific dining hall **(WIP)** |
| GET    | /api/menus/:diningHall/lunch             | Retrieve lunch menu for specific dining hall **(WIP)**     | 
| GET    | /api/menus/:diningHall/dinner            | Retrieve dinner menu for specific dining hall **(WIP)**    | 

### Example Requests
- Retrieve breakfast menu
  ```bash
  curl -X GET http://localhost:5000/api/menus/breakfast```

## Contributions
Contributions are welcome! Please follow these steps to contribute:
1. Fork the repository.
2. Create a new branch: git checkout -b feature/your-feature-name.
3. Make your changes and commit them: git commit -m 'Add some feature'.
4. Push to the branch: git push origin feature/your-feature-name.
5. Submit a pull request.
