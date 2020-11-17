from django.urls import path, include
from django.views.i18n import JavaScriptCatalog

from wagtail.core import hooks


@hooks.register("register_admin_urls")
def register_admin_urls():
    urls = [
        path('jsi18n/', JavaScriptCatalog.as_view(packages=['wagtail_foo']), name='javascript_catalog'),

        # Add your other URLs here, and they will appear under `/admin/foo/`
        # Note: you do not need to check for authentication in views added here, Wagtail does this for you!
    ]

    return [
        path(
            "foo/",
            include(
                (urls, "wagtail_foo"),
                namespace="wagtail_foo",
            ),
        )
    ]
