Bloom Filters over HTTP for remote access.

# Usage
```
$ git clone https://github.com/assafmo/BloomREST.git
$ cd BloomREST
$ cat > values
google.com
banana
papaya
^C
$ maxItems=100
$ falsePositiveRate=0.00001 # 0.001%
$ bloomFile=/path/to/new/test.bloom
$ cat values | ./ingest.py $bloomFile $maxItems $falsePositiveRate # if $bloomFile already exists - just add the values to it
$ port=4096
$ ./serve.py $bloomFile $port 2> /dev/null &
$ curl http://localhost:4096/check -d '["banana","papaya","google.com","batman!"]'
[true,true,true,false]
$ curl http://localhost:4096/add -d '["batman!"]'
$ curl http://localhost:4096/check -d '["banana","papaya","google.com","batman!"]'
[true,true,true,true]
```