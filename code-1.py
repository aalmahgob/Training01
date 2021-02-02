Python 3.9.1 (v3.9.1:1e5d33e9b9, Dec  7 2020, 12:10:52) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> u=1
>>> 'u=1
SyntaxError: EOL while scanning string literal
>>> u=1, r=2, u+r
SyntaxError: cannot assign to literal
>>> r=2
>>> u+r
3
>>> 