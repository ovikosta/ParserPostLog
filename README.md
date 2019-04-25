# Parser postfix log.

This package can parse postfix logfile and count the number of sent letters.
Script take a logfile to the input function and create new file with result parse.

##### For use this script execute the following commands:
```
git clone https://github.com/ovikosta/parserlog.git
cd ./parserlog
pip install .
```

##### Now start python interpreter and import install parserlog:
```
import parserlog.engine as parser
result = parser.parse('/path/to/filelog')
parser.write_in_file(result[0], result[1], result[2])
```
After execute this command in folder a new file appears with name result.
