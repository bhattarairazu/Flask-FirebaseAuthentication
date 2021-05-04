# JourneyFoods AI
---
This repository contains the code for providing recommendations and managing backend server for JourneyFoods Recommendation Engine.

## Getting Started
These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites
```
1. Linux
2. Python3
3. Virtualenv
4. MongoDB
```

### Installation
1. Create `Virtualenv` for your project.

    `virtualenv -p python3 .venv`
2. Activate the Virtual Environment.

    `source .venv/bin/activate`
3. Install the requirements files
    ```bash
    pip install -r requirements.txt
    ```
4. Add provided `.csv` files into `data/processed` folder.

    Files can be `usda.csv`, `non_product_complete_data.csv`, or `non_product_curated_data.csv` as required.

## Usage
1. Run the micro-service application

    `flask run -h 0.0.0.0`

    It runs the application on `0.0.0.0:5000` port.

2. Go to `<IP>:5000` to get the SWAGGER API Documentation

    or

    Use the provided POSTMAN collection to access the services.

## Running the tests
To run all the tests

`pytest`

## Contributing
Please read [CONTRIBUTING.md](CONTRIBUTING.md) for details on our code of conduct, and the process for submitting pull requests to us.

## Versioning
We use [SemVer](http://semver.org/) for versioning. For the versions available, see the [tags on this repository](https://github.com/your/project/tags).

## License
This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details
