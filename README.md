
# REST API Public Fetch

## Overview
This Python application asynchronously retrieves vehicle variable data from the NHTSA public REST API and displays only records whose `GroupName` is `Active Safety System`.

## Run
Install the dependency:

```bash
python -m pip install aiohttp
```

Then run:

```bash
python public_fetch.py
```

## Reflection
In this assignment, I created a Python application that retrieves vehicle information from a public REST API. I started by identifying the NHTSA endpoint and using an asynchronous GET request to retrieve its data. The program then converts the response into JSON and checks the Results list. I added a filter so that only records with a GroupName of "Active Safety System" appear in the output. I also included a loading message and error handling for connection problems, timeouts, and invalid responses.

What surprised me was how much information one public API can provide and how a small filter can make that information more useful. My code evolved from simply retrieving the data to selecting specific records and displaying their details clearly. This assignment helped me better understand asynchronous programming, JSON objects, REST endpoints, and the technical layer of interoperability. I would like to learn more about displaying API results in a graphical interface and automatically refreshing the information.
