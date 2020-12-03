<!--
https://readme42.com
-->


[![](https://img.shields.io/pypi/v/gfm2html.svg?maxAge=3600)](https://pypi.org/project/gfm2html/)
[![](https://img.shields.io/badge/License-Unlicense-blue.svg?longCache=True)](https://unlicense.org/)
[![](https://github.com/andrewp-as-is/gfm2html.py/workflows/tests42/badge.svg)](https://github.com/andrewp-as-is/gfm2html.py/actions)

### Installation
```bash
$ [sudo] pip install gfm2html
```

#### Pros
100% true native github flavored markdown

#### How it works
[github markdown api](https://developer.github.com/v3/markdown/)

#### Examples
```python
from gfm2html import gfm2html

gfm2html(markdown) # For unauthenticated requests, the rate limit allows for up to 60 requests per hour
gfm2html(markdown, token="XXX")
```

#### Links
+   [github markdown api](https://developer.github.com/v3/markdown/)

<p align="center">
    <a href="https://readme42.com/">readme42.com</a>
</p>
