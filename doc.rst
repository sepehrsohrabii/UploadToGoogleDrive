
Prerequisites
*************

To use this storage, you have to:

* `set up a project and application in the Google Developers Console <https://console.developers.google.com/flows/enableapi?apiid=drive>`_
* `obtain the json private key file (OAuth 2.0 for Server to Server Applications) for your Google Project associated with Google Drive service <https://developers.google.com/identity/protocols/OAuth2ServiceAccount>`_

Installation
************

This storage is hosted on `PyPI <https://pypi.python.org/pypi/django-googledrive-storage>`_. It can be easily installed
through *pip*:

.. code-block:: bash

   pip install django-googledrive-storage

Setup
*****

Once installed, there are a few steps to configure the storage:

* add the module *gdstorage* to your installed apps in your `settings.py` file:

.. code-block:: python

   INSTALLED_APPS = (
       ...,
       'django.contrib.staticfiles',
       'gdstorage'
   )

* create a section in your `setting.py` that contains the configuration for this storage:

.. code-block:: python

   #
   # Google Drive Storage Settings
   #

   GOOGLE_DRIVE_STORAGE_JSON_KEY_FILE = '<path to your json private key file>'
   GOOGLE_DRIVE_STORAGE_MEDIA_ROOT = '<base google drive path for file uploads>' # OPTIONAL

The `GOOGLE_DRIVE_STORAGE_JSON_KEY_FILE` must be the path to *private json key file* obtained by Google. |br|
Alternatively, you can place the contents of your json private key file into an environment variable named
`GOOGLE_DRIVE_STORAGE_JSON_KEY_FILE_CONTENTS`, this requires setting `GOOGLE_DRIVE_STORAGE_JSON_KEY_FILE` to `None`.

The `GOOGLE_DRIVE_STORAGE_MEDIA_ROOT` is analogous to MEDIA_ROOT for django’s built-in FileSystemStorage


* Then replace the begoodPlus/morders/admin.py and begoodPlus/morders/models.py with the files that we prepared.

* migrate the database.
** for more information you should create a project in google console, activate the google drive api, create a service certificate, and when you open that certificate page there will be a key option that you can generate the needed key there and take it in the repository of your project after that use it path in the settings.py .