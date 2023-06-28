# BugnaughtBE

Python/Flask backend for Bugnaught project

## MySQL data storage

This app stores data with MySQL hosted on PlanetScale. It is my first foray into MySQL, and I have discovered it has its quirks.

## API Routes

Intended as a RESTful API that serves JSON data to be consumed by Bugnaught, a bug tracker app, here are the supported endpoints:

* GET Bugnaught projects

['http://localhost:3000/api/projects'](http://localhost:3000/api/projects)

* GET Bugnaught users

['http://localhost:3000/api/users'](http://localhost:3000/api/users)
