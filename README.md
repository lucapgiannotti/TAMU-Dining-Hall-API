# TAMU Dining Halls Menu API

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
- [Donate](#donate)

## Introduction
The TAMU Dining Halls Menu API allows users to retrieve the daily menu for various dining halls at Texas A&M University. It supports querying for breakfast, lunch, and dinner menus.

## Features
- Retrieve daily menus for breakfast, lunch, and dinner.
- Filter menus by specific dining halls.
- Easy-to-use RESTful API endpoints.

## Installation
To run this API locally using Flask, follow these steps:

1. **Clone the repository:**
```bash
   git clone https://github.com/Squidnugget77/TAMU-Dining-Hall-API.git
   cd TAMU-Dining-Hall-API
```
2. **Create a virtual environment**
```bash
   python3 -m venv venv
   source venv/bin/activate   # On Windows use `venv\Scripts\activate`
```
3. **Install depedencies**
```bash
   pip install -r requirements.txt
```

3. **Make changes to run locally**
   If using Windows, comment lines 13-16 in `web_scraper.py`.

## Usage
### Endpoints
| Method | Endpoint                                 | Description                                      |
|--------|------------------------------------------|--------------------------------------------------|
| GET    | /:diningHall/breakfast         | Retrieve breakfast menu for a specific dining hall  |
| GET    | /:diningHall/lunch             | Retrieve lunch menu for a specific dining hall | 
| GET    | /:diningHall/dinner            | Retrieve dinner menu for a specific dining hall   | 

### Example Requests
- Retrieve The Commons Dining Hall breakfast menu
```bash
  curl -X GET http://api.lucagiannotti.com/commons/breakfast
```

- Retrieve Sbisa Dining Hall lunch menu
```bash
  curl -X GET http://api.lucagiannotti.com/sbisa/lunch
```

## Contributing
Contributions are welcome! Please follow these steps to contribute:
1. Fork the repository.
2. Create a new branch: git checkout -b feature/your-feature-name.
3. Make your changes and commit them: git commit -m 'Add some feature'.
4. Push to the branch: git push origin feature/your-feature-name.
5. Submit a pull request.

## Donate
<a href="https://www.buymeacoffee.com/lucagiannotti"><img src="https://img.buymeacoffee.com/button-api/?text=Buy me a coffee&emoji=&slug=xeroKun&button_colour=ed966d&font_colour=FFFFFF&font_family=Lato&outline_colour=000000&coffee_colour=ffffff" /></a>

Each donation is greatly appreciated, but not expected. However, if you enjoy this API, each donation goes towards hosting this service that is publically available. Thank you!
