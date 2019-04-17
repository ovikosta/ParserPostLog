#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import re


class EngineParser:
    def __init__(self, file):
        self.file = file

    def parse(self):
        pattern_id = re.compile('([A-Z0-9]{11})')
        pattern_from = re.compile('[a-zA-Z0-9._%+-]+@([a-zA-Z0-9.-]+)(\.[a-zA-Z]{2,4})') #add from in search
        with open("log") as file_log:
            for line in file_log:
                id_field = pattern_id.match(line)