Bloom Filters over REST HTTP server for remote access.  
This probably should not be exposed to end users. :-)  

# Usage
```bash
git clone https://github.com/assafmo/BloomREST.git
cd BloomREST

pip install pybloomfiltermmap
# or: apt install python-pybloomfiltermmap

cat values
# => 
# google.com
# banana
# papaya

maxItems=100
falsePositiveRate=0.00001 # 0.001%
bloomFile=/path/to/new/test.bloom

# if $bloomFile already exists - ignore $maxItems $falsePositiveRate and just add the values to it
cat values | ./ingest.py $bloomFile $maxItems $falsePositiveRate 

port=4096
./serve.py $bloomFile $port 2> /dev/null &

curl http://localhost:4096/check -X POST -d '["banana","papaya","google.com","batman!"]'
# =>
# [true,true,true,false]

curl http://localhost:4096/add -X POST -d '["batman!"]'

curl http://localhost:4096/check -X POST -d '["banana","papaya","google.com","batman!"]'
# =>
# [true,true,true,true]
```

# License
[MIT](/LICENSE.md)
