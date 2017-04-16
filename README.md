# ProdManager - Production Manager
This app manage a production server based on Docker.

## Deployment
You can deploy this app by using Docker

## Project structure
The goal of this app is to manage payments acting and logging for other apps of BdE INSA Lyon. But if it fits your needs
you are free to use it.

The application is divided into four django application that are not splittable.

- api: This app is designed to store API presented to our applications and interact with other parts
- applications: This is the application authorisation and logging logic. Every access through API is authorized by this
   app.
- gateway: If a payment require an external interaction, this app keep track of the user and redirect him through
    payments pages of the gateway.
- trezo: This app register all payments and allow managers to list payments and export data about them.

account and permissions are BdE INSA Lyon's commons package to manage user login and permission management.

## CLI
This project has a CLI available with cli.pm

## Licence
[![GNU GPL v3.0](http://www.gnu.org/graphics/gplv3-127x51.png)](http://www.gnu.org/licenses/gpl.html)

```
ProdManager - Production Manager
Copyright (C) 2017 Philippe VIENNE
Copyright (C) 2017 Gabriel AUGENDRE
Copyright (C) 2017 BdE INSA Lyon

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.