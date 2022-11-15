
# Formatting tests:

""  # codeql
""  # codeql[py/line-too-long]
""  # codeql[py/line-too-long, py/non-callable-called]
""  # codeql[@tag:security]
""  # codeql[@tag:security,py/line-too-long]
""  # codeql[@expires:2017-06-11]
""  # codeql[py/non-callable-called] because I know better than codeql
""  # codeql: blah blah
""  # codeql blah blah #falsepositive
""  # codeql blah blah -- falsepositive
""  # codeql  [py/non-callable-called]
""  # codeql[]
""  # codeqlfoo
""  # codeql
""  # codeql
""  # codeql    [py/line-too-long]
""  # codeql codeql


# codeql -- Ignore this -- No line or scope.

# On real code:

def foo():  # codeql [func]
    # codeql -- Blank line (ignore for now, maybe scope wide in future).
    "docstring"  # codeql on docstring
    return {  # codeql [py/duplicate-key-in-dict]
        "a": 1,
        "a": 2
    }


class C:  # codeql class
    def meth(self):  # codeql method
        pass


""  # noqa
""  # noqa

"The following should be ignored"
""  # flake8: noqa
""  # noqa: F401
""  # noqa -- Some extra detail.
""  # Ignore

# Suppression for multiple tools
# codeql-1929


class frozenbidict(BidictBase):  # noqa: E501; (line too long) pylint: disable=invalid-name; codeql [py/missing-equals]
    pass


""  # noqa: E501; (line too long) pylint: disable=invalid-name; codeql
""  # random nonsense codeql [py/missing-equals] and then some more commentary...


# Case insensitive comments

""  # codeql
""  # codeql[py/line-too-long]

# Avoid some erroneous matches
""  # foocodeql[py/missing-equals]
""  # foocodeql

""  # codeql[py/line-too-long] and codeql[py/non-callable-called]
""  # codeql[py/line-too-long]; codeql
