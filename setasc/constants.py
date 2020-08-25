import re

CLASSIFIERS = re.compile(r"classifiers=\[[^\]]*\]", re.DOTALL)
CLASSIFIERS_LIST = re.compile(r"classifiers=\[([^\]]*)\]", re.DOTALL)
SETUP = re.compile(r"setup\(.*\)", re.DOTALL)

BINOPS = dict(Add="+")

SETUP_KEYWORD_ARGUMENTS = [
    "name",
    "version",
    "description",
    "long_description",
    "long_description_content_type",
    "author",
    "author_email",
    "maintainer",
    "maintainer_email",
    "url",
    "download_url",
    "packages",
    "py_modules",
    "scripts",
    "ext_package",
    "ext_modules",
    "classifiers",
    "distclass",
    "script_name",
    "script_args",
    "options",
    "license",
    "keywords",
    "platforms",
    "cmdclass",
    "package_dir",
    "include_package_data",
    "exclude_package_data",
    "package_data",
    "zip_safe",
    "install_requires",
    "entry_points",
    "extras_require",
    "python_requires",
    "namespace_packages",
    "test_suite",
    "tests_require",
    "test_loader",
    "eager_resources",
    "use_2to3",
    "convert_2to3_doctests",
    "use_2to3_fixers",
    "use_2to3_exclude_fixers",
    "project_urls",
]
