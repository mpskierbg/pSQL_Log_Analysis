#!/usr/bin/env python
from news import SqlPython

first = SqlPython()
first.most_popular_articlex3()

second = SqlPython()
second.most_popular_author()

third = SqlPython()
third.most_errors()
