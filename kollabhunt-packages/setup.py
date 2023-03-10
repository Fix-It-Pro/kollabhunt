import setuptools

setuptools.setup(
    name="kollabhunt-lib",
    version="0.0.1",
    description="testing migrations",
    long_description="description",
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
    include_package_data=True,
    install_requires=[
        'asgiref==3.6.0',
        'backports.zoneinfo==0.2.1',
        'Django==4.1.6',
        'django-social-auth==0.7.28',
        'djangorestframework==3.14.0',
        'djangorestframework-simplejwt==5.2.2',
        'httplib2==0.21.0',
        'oauth2==1.9.0.post1',
        'psycopg2-binary==2.9.5',
        'PyJWT==2.6.0',
        'pyparsing==3.0.9',
        'python-dotenv==0.21.1',
        'python-openid==2.2.5',
        'pytz==2022.7.1',
        'sqlparse==0.4.3',
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        # "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
