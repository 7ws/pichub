class AuthenticationSettings:
    """
    Settings related to authentication throughout all apps
    """

    AUTH_PASSWORD_VALIDATORS = [
        {'NAME': f'django.contrib.auth.password_validation.{name}'}
        for name in [
            'UserAttributeSimilarityValidator',
            'MinimumLengthValidator',
            'CommonPasswordValidator',
            'NumericPasswordValidator',
        ]
    ]

    AUTHENTICATION_BACKENDS = (
        # Needed to login by username in Django admin, regardless of `allauth`
        'django.contrib.auth.backends.ModelBackend',

        # `allauth` specific authentication methods, such as login by e-mail
        'allauth.account.auth_backends.AuthenticationBackend',
    )

    # django-allauth providers
    SOCIALACCOUNT_PROVIDERS = {
        'google': {
            'SCOPE': [
                'profile',
                'email',
            ],
            'AUTH_PARAMS': {
                'access_type': 'online',
            }
        },
    }
