#!/usr/bin/env python
# encoding: utf-8
"""
LexbaseDecoder.py
Created by Magnus Wahlberg on 2014-01-27.
"""

import sys
import csv

year = {"a":"X", "b":"8", "c":"X", "d":"X", "e":"X", "f":"X", "g":"2", "h":"3", "i":"X", "j":"4", "k":"5", "l":"X", "m":"6", "n":"7", "o":"X", "p":"X", "q":"1", "r":"X", "s":"X", "t":"X", "u":"X", "v":"9", "w":"0", "x":"X", "y":"X", "z":"X"}

month = {"a":"X", "b":"8", "c":"X", "d":"X", "e":"X", "f":"X", "g":"2", "h":"3", "i":"X", "j":"X", "k":"5", "l":"X", "m":"X", "n":"7", "o":"6", "p":"X", "q":"1", "r":"X", "s":"X", "t":"X", "u":"4", "v":"9", "w":"0", "x":"X", "y":"X", "z":"X"}

date = {"a":"2", "b":"8", "c":"X", "d":"X", "e":"X", "f":"X", "g":"X", "h":"X", "i":"5", "j":"X", "k":"X", "l":"X", "m":"X", "n":"X", "o":"6", "p":"X", "q":"1", "r":"X", "s":"9", "t":"3", "u":"4", "v":"X", "w":"0", "x":"X", "y":"X", "z":"7"}

number = {"a":"2", "b":"X", "c":"0", "d":"-", "e":"X", "f":"1", "g":"X", "h":"X", "i":"5", "j":"X", "k":"X", "l":"X", "m":"X", "n":"X", "o":"6", "p":"X", "q":"X", "r":"X", "s":"9", "t":"3", "u":"4", "v":"X", "w":"X", "x":"8", "y":"X", "z":"7"}

def loadcsv(csvfile):
	return csv.reader(csvfile)

def decode_number(str):
	decoded = ""
	if len(str) > 12:
		cleaned_str = str[10:]
	else:
		cleaned_str = str[8:]

	for char in cleaned_str:
		decoded += number[char]
	return decoded

def decode_date(str):
	decoded = ""
	if len(str) > 12:
		cleaned_str = str[7:9]
	else:
		cleaned_str = str[5:7]

	for char in cleaned_str:
		decoded += date[char]
	return decoded

def decode_month(str):
	decoded = ""
	if len(str) > 12:
		cleaned_str = str[5:7]
	else:
		cleaned_str = str[3:5]

	for char in cleaned_str:
		decoded += month[char]
	return decoded

def decode_year(str):
	decoded = ""
	if len(str) > 12:
		cleaned_str = str[1:5]
	else:
		cleaned_str = str[1:3]

	for char in cleaned_str:
		decoded += year[char]
	return decoded

def checkKey(key):
	for key, value in key.iteritems():
		if value != "X":
			print value


def main():
	coded = sys.argv[1]

	Year =  decode_year(coded)
	
	Month = decode_month(coded)
	
	Date = decode_date(coded)
	
	Number = decode_number(coded)
	
	fullPersonNr = Year+Month+Date+"-"+Number

	print fullPersonNr

if __name__ == '__main__':
	main()
