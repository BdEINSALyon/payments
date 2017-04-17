.. Payments documentation master file, created by
   sphinx-quickstart on Wed Mar 22 11:57:35 2017.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to Payments's documentation!
====================================

This document describe the logic behind this Payment manager application.

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

.. toctree::
   :maxdepth: 2
   :caption: Contents:

   setup


Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
