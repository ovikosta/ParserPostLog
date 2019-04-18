#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import re
from collections import Counter


class EngineParser:
    def __init__(self, file):
        self.file = file

    def parse(self):
        pattern_id = re.compile(r'([A-Z0-9]{11})(?=:)')
        pattern_from = re.compile(r'(?<=from=<)[a-zA-Z0-9._%+-]+@([a-zA-Z0-9.-]+)(\.[a-zA-Z]{2,4})(?=>)')
        tmp_store = dict()
        count_ok, count_fail = Counter()
        st_sent = 'sent'
        with open(self.file, 'r') as file_log:
            for line in file_log:
                id_field = pattern_id.match(line)
                from_field = pattern_from.match(line)
                if id_field and from_field:
                    #add key:value to temp dict
                    tmp_store[id_field] = from_field
                elif 'status' in line:
                    #check status in line
                    if st_sent in line:
                        count_ok[tmp_store[id_field]] += 1
                    else:
                        count_fail[tmp_store[id_field]] += 1
                elif 'removed' in line:
                    del tmp_store[id_field]
                id_field = None
                from_field = None
            count_total = count_ok + count_fail
        return count_ok, count_fail, count_total


