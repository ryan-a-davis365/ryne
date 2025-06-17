# **Deployment**

## **Table of Contents**

* [**Deployment**](#deployment)
  * [**Table of Contents**](#table-of-contents)
  * [**Initial Deployment**](#initial-deployment)
    * [**Create repository**](#create-repository)
    * [**Setting up the Workspace** (To be done locally via the console of your chosen editor)](#setting-up-the-workspace-to-be-done-locally-via-the-console-of-your-chosen-editor)
    * [**Create Heroku App**](#create-heroku-app)
    * [**AWS S3 Bucket**](#aws-s3-bucket) 
    * [**Creating Environmental Variables Locally**](#creating-environmental-variables-locally)
    * [**Setting up setting.py File**](#setting-up-settingpy-file)

## **Initial Deployment**

Below are the steps I took to deploy the site to Heroku and any console commands required to initiate it.

### **Create repository**

1. Create a new repository in GitHub and clone it locally following [these instructions](https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository)
    * ***Note*** - If you are cloning my project, then you can skip all pip installs below and just run the following command in the terminal to install all the required libraries/packages at once:
       * ```pip install -r requirements.txt```
    * ***IMPORTANT*** -  If developing locally on your device, ensure you set up/activate the virtual environment ([see below](#setting-up-the-workspace-to-be-done-locally-via-the-console-of-your-chosen-editor)) before installing/generating the requirements.txt file; failure to do this will pollute your machine and put other projects at risk


### **Setting up the Workspace** (To be done locally via the console of your chosen editor)

1. Create a virtual environment on your machine:
    * python -m venv .venv
1. To ensure the virtual environment is not tracked by version control, add .venv to the .gitignore file.
1. Install Django with version 3.2:
    * ```pip install django==5.2```
1. Install gunicorn:
    * ```pip install gunicorn```
1. Install supporting libraries:
    * ```pip install dj_database_url```
    * ```pip install psycopg2-binary```
1. Create requirements.txt:
    * ```pip freeze --local > requirements.txt```
1. Create an empty folder for your project in your chosen location.
1. Create a project in the above folder:
    * ```django-admin startproject <PROJECT_NAME>``` (in the case of this project, the project name was "ryne")
1. Create an app within the project:
    * ```python manage.py startapp APP_NAME``` (in the case of this project, the app name was "home")
1. Add a new app to the list of installed apps in setting.py
1. Migrate changes:
    * ```python manage.py migrate```
1. Test server works locally:
    * ```python manage.py runserver```  (You should see the default Django success page)

### **Create Heroku App**

The below works on the assumption that you already have an account with [Heroku](https://id.heroku.com/login) and are already signed in.

1. Create a new Heroku app:
    * Click "New" in the top right-hand corner of the landing page, then click "Create new app."
1. Give the app a unique name:
    * Will form part of the URL (in the case of this project, I called the Heroku app ryne)
1. Select the nearest location:
    * For me, this was Europe.
1. Head to "Deploy" and then "Deployment Method" and select GitHub then select the correct repository.
    * In this case it was RYNE.
1. Add Database to the Heroku app:
    * Navigate to the Settings tab of the Heroku dashboard, then head to Config Vars and add DATABASE_URL
    * left box under config vars (variable KEY) = DATABASE_URL
    * right box under config vars (variable VALUE) = Postgresql database link
1. From your editor, go to your projects settings.py file and copy the SECRET_KEY variable. Add this to the same name variable under the Heroku App's config vars.
    * left box under config vars (variable KEY) = SECRET_KEY
    * right box under config vars (variable VALUE) = Value copied from settings.py in project.

### **AWS S3 Bucket**

The below works on the assumption that you already have an account with [AWS](https://signin.aws.amazon.com/signin?redirect_uri=https%3A%2F%2Fus-east-1.console.aws.amazon.com%2Fconsole%2Fhome%3FhashArgs%3D%2523%26isauthcode%3Dtrue%26nc2%3Dh_ct%26region%3Dus-east-1%26skipRegion%3Dtrue%26src%3Dheader-signin%26state%3DhashArgsFromTB_us-east-1_5ebca9aa1f981aaf&client_id=arn%3Aaws%3Asignin%3A%3A%3Aconsole%2Fcanvas&forceMobileApp=0&code_challenge=tXaJuB6g7gFkIttyTd75shZNQrYlt0B3-zdaKPesuQI&code_challenge_method=SHA-256) and are already signed in.

1. Create a new S3 bucket:
    The AWS S3 documentation helped me set this up [AWS Documentation](https://docs.aws.amazon.com/AmazonS3/latest/userguide/GetStartedWithS3.html)
1. Amend Bucket settings:
    * Bucket Properties: -
       * Click on the bucket name to open the bucket.
       * Click on the "Properties" tab.
       * Under the "Static website hosting" section, click "Edit."
       * Under the "Static website hosting" section select "Enable".
       * Under the "Hosting type" section ensure "Host a static website" is selected.
       * Under the "Index document" section enter "index.html".
       * Click "Save changes."
    * Bucket Permissions: -
       * Click on the "Permissions" tab.
       * Scroll down to the "CORS configuration" section and click edit.
       * Enter the following snippet into the text box:

        ```JSON
            [
                {
                    "AllowedHeaders": [
                        "Authorization"
                    ],
                    "AllowedMethods": [
                        "GET"
                    ],
                    "AllowedOrigins": [
                        "*"
                    ],
                    "ExposeHeaders": []
                }
            ]
        ```

       * Click "Save changes."
       * Scroll back up to the "Bucket Policy" section and click "Edit."
       * Take note of the "Bucket ARN" click on the "Policy Generator" button to open the AWS policy generator in a new tab.
       * In the newly opened tab under Step 1 "Select Policy Type" select "S3 Bucket Policy." from the drop down menu.
       * Under Step 2 "Add Statement(s)" enter " * " in the "Principal" text box.
       * From the "s3:Action" drop down menu select "s3:GetObject".
       * Enter the "ARN" noted from the bucket policy page into the "Amazon Resource Name (ARN)" text box.
       * Click "Add Statement."
       * Under Step 3 "Generate Policy" click "Generate Policy."
       * Copy the resultant policy and paste it into the bucket policy text box on the previous tab.
       * In the same text box add "/*" to the end of the resource key to allow access to all resources in this bucket.
       * Click "Save changes."
       * When back on the buckets permissions tab, scroll down to the "Access Control List" section and click "Edit."
       * enable "List" for "Everyone (public access)", tick the box to accept that "I understand the effects of these changes on my objects and buckets."  and click "Save changes."

    1. Create AWS static files User and assign to S3 Bucket:
    * Create "User Group": -
        * Click "Services" in the top left-hand corner of the landing page, from the left side of the menu click on "Security, Identity, & Compliance" and select "IAM" from the right side of the menu.
        * Under "Access management" click "User Groups."
        * Click "Create Group."
        * Enter a user name (in the case of this project, I called the user group "projectryne-group").
        * Scroll to the bottom of the page and click "Create Group."
    * Create permissions policy for the new user group: -
        * Click "Policies" in the left-hand menu.
        * Click "Create Policy."
        * Click "Import managed policy."
        * Search for "AmazonS3FullAccess", select this policy, and click "Import".
        * Click "JSON" under "Policy Document" to see the imported policy
        * Copy the bucket ARN from the bucket policy page and paste it into the "Resource" section of the JSON snippet. Be sure to remove the default value of the resource key ("*") and replace it with the bucket ARN.
        * Copy the bucket ARN a second time into the "Resource" section of the JSON snippet. This time, add "/*" to the end of the ARN to allow access to all resources in this bucket.
        * Click "Next: Tags."
        * Click "Next: Review."
        * Click "Review Policy."
        * Enter a name for the policy (in the case of this project, I called the policy "projectryne-policy").
        * Enter a description for the policy.
        * Click "Create Policy."
    * Attach Policy to User Group: -
        * Click "User Groups" in the left-hand menu.
        * Click on the user group name created during the above step.
        * Select the "Permissions" tab.
        * Click "Attach Policy."
        * Search for the policy created during the above step, and select it.
        * Click "Attach Policy."
    * Create User: -
        * Click "Users" in the left-hand menu.
        * Click "Add user."
        * Enter a "User name" (in the case of this project, I called the user "projectryne-user").
        * Select "Programmatic access" and "AWS Management Console access."
        * Click "Next: Permissions."
        * Select "Add user to group."
        * Select the user group created during the above step.
        * Click "Next: Tags."
        * Click "Next: Review."
        * Click "Create user."
        * Take note of the "Access key ID" and "Secret access key" as these will be needed to connect to the S3 bucket.
        * Click "Download .csv" to download the credentials.
        * Click "Close."
1. Install required packages to used AWS S3 Bucket in Django:
    * ```pip install boto3```
    * ```pip install django-storages```
1. Add 'storages' to the bottom of the installed apps section of settings.py file:

   ```python
    INSTALLED_APPS = [
    …,
        'storages'
    …,
   ]
   ```

### **Creating Environmental Variables Locally**

1. Install dotenv package:
    * ```pip install python-dotenv```
1. On your local machine, create a file called ".env" at the same level as settings.py and add this to the .gitignore file.
1. From your projects settings.py file, copy the SECRET_KEY value and assign it to a variable called SECRET_KEY in your .env file
    * ``` SECRET_KEY=PastedValueFromYourProjectsSettings.pyFile ```

### **Setting up setting.py File**

1. At the top of your settings.py file, add the following snippet immediately after the other imports:

    ```python
        from pathlib import Path
        import os
        import dj_database_url
        if os.path.isfile('env.py'):
            import env

        SECRET_KEY = os.environ.get("SECRET_KEY")
    ```

1. Add this line in settings.py to link your postgresql database.

    ``` python
        DATABASES = {
        'default': dj_database_url.parse(os.environ.get("DATABASE_URL"))
        }
    ```

1. Tell Django to where to store media and static files by placing this snippet under the comments indicated below, it can look confusing at first but the if block just means to first use the aws s3 storage bucket previously created for images before trying local static files.

    ```python
        STATIC_URL = '/static/'
        STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
        STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

        USE_AWS = os.environ.get('USE_AWS') == 'True'

        if USE_AWS:
            MEDIA_URL = (
                f'https://{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com/media/products/'
            )
        else:
            MEDIA_URL = '/media/products/'
            MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
    ```

1. Add the following snippet to the end of the urlpatterns list:

    ``` python
       urlpatterns =[
            path('admin/', admin.site.urls),
        ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    ```

1. Within TEMPLATES array, add ``` 'DIRS':[TEMPLATES_DIR] ``` like the below example:

   ```python
      TEMPLATES = [
        {
            'BACKEND': 'django.template.backends.django.DjangoTemplates',
            'DIRS': [
                os.path.join(BASE_DIR, 'templates'),
            ],
        }
    ]
   ```

1. Link S3 Bucket to Django Project by adding the following to the settings.py file:
```python
    AWS_S3_OBJECT_PARAMETERS = {
            'Expires': 'Thu, 31 Dec 2099 20:00:00 GMT',
            'CacheControl': 'max-age=94608000',
    }
    AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
    AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')
    AWS_STORAGE_BUCKET_NAME = os.environ.get('AWS_STORAGE_BUCKET_NAME')
    AWS_S3_REGION_NAME = 'eu-north-1'
    AWS_S3_CUSTOM_DOMAIN = 'projectryne.s3.amazonaws.com'

    STATIC_URL = '/static/'
    MEDIAFILES_LOCATION = 'media/'

    USE_AWS = os.environ.get('USE_AWS') == 'True'

    if USE_AWS:
        MEDIA_URL = (
            f'https://{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com/media/products/'
        )
    else:
        MEDIA_URL = '/media/products/'
        MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
```

1. Add allowed hosts to settings.py:
    * ``` ALLOWED_HOSTS = ['PROJECT_NAME.herokuapp.com', '127.0.0.1', 'localhost'] ```

1. Create Procfile at the top level of the file structure and insert the following:
    * ``` web: gunicorn PROJECT_NAME.wsgi ```

1. Make an initial commit and push the code to the GitHub Repository.
    * ```git add .```
    * ```git commit -m "Initial deployment"```
    * ```git push```

1. Add AWS Keys to Heroku Config Vars.

1. Add the ```USE_AWS``` variable to Heroku Config Vars and set it to True.

1. Create a file call "Custom_storages.py" in the root of the project and add the following code:

```python
    from django.conf import settings
    from storages.backends.s3boto3 import S3Boto3Storage


    class MediaStorage(S3Boto3Storage):
        location = 'media'
        file_overwrite = False
```

[Back to Readme](README.md)