"""OpenLine documentation."""

import os

GITHUB = (
    '<svg viewBox="0 0 16 16" fill="currentColor"><path fill-rule="evenodd" d="M8 0C3.58 0 0 '
    "3.58 0 8c0 3.54 2.29 6.53 5.47 7.59.4.07.55-.17.55-.38 0-.19-.01-.82-.01-1.49-2.01.37-2.53"
    "-.49-2.69-.94-.09-.23-.48-.94-.82-1.13-.28-.15-.68-.52-.01-.53.63-.01 1.08.58 1.23.82.72 1.21"
    " 1.87.87 2.33.66.07-.52.28-.87.51-1.07-1.78-.2-3.64-.89-3.64-3.95 0-.87.31-1.59.82-2.15-.08"
    "-.2-.36-1.02.08-2.12 0 0 .67-.21 2.2.82.64-.18 1.32-.27 2-.27.68 0 1.36.09 2 .27 1.53-1.04"
    " 2.2-.82 2.2-.82.44 1.1.16 1.92.08 2.12.51.56.82 1.27.82 2.15 0 3.07-1.87 3.75-3.65 3.95.29"
    ".25.54.73.54 1.48 0 1.07-.01 1.93-.01 2.2 0 .21.15.46.55.38A8.013 8.013 0 0 0 16 8c0-4.42"
    '-3.58-8-8-8z"/></svg>'
)

project = "OpenLine"
html_title = "OpenLine"
extensions = ["myst_parser", "sphinx_copybutton", "openline_sphinx"]
myst_enable_extensions = ["colon_fence", "deflist"]
copybutton_selector = "div:not(.openline-output) > div.highlight > pre"
html_theme = "furo"
html_theme_options = {
    "top_of_page_buttons": [],
    "navigation_with_keys": True,
    "footer_icons": [
        {
            "name": "GitHub",
            "url": "https://github.com/BirchfieldResearchGroup/openline",
            "html": GITHUB,
        }
    ],
}
html_baseurl = os.environ.get("READTHEDOCS_CANONICAL_URL", "")  # each page's canonical link
html_extra_path = ["_extra"]  # llms.txt, which Read the Docs serves at the root of the domain
html_use_index = False
html_domain_indices = False
html_copy_source = False
html_show_copyright = False
html_show_sourcelink = False
nitpicky = True
nitpick_ignore_regex = [(r"py:.*", r"(?!openline).*")]  # Python's own types are not linked
exclude_patterns = ["_build"]
autodoc_typehints = "signature"
autodoc_typehints_format = "short"
autodoc_preserve_defaults = True
autodoc_member_order = "bysource"
autodoc_inherit_docstrings = False
add_module_names = False
python_maximum_signature_line_length = 88
toc_object_entries_show_parents = "hide"
openline_sources = "../sources"
openline_examples = "../examples"
openline_catalog = True
