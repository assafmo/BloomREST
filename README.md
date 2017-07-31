Bloom Filters over REST API for remote access.  
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
# Docker
[https://hub.docker.com/r/assafmo/bloomrest-ingest](https://hub.docker.com/r/assafmo/bloomrest-ingest)  
[https://hub.docker.com/r/assafmo/bloomrest-serve](https://hub.docker.com/r/assafmo/bloomrest-serve)

```
# Create a bloom filter with one value "test1" on your local filesystem ./my.bloom
echo test1 | docker run -i -v $PWD:/data/ assafmo/bloomrest-ingest my.bloom 10 0.001

# Make ./my.bloom your own
sudo chown $USER:$USER my.bloom

# Mount the directory with ./my.bloom (currently $PWD) to /data/ and pass the new my.bloom path and 4096 as a port to docker (must be 4096!)
docker run -d -p 1111:4096 -v $PWD:/data/ assafmo/bloomrest-serve /data/my.bloom 4096

curl http://localhost:1111/check -d '["test1","test2"]'                                      
# =>
# [true, false]
```

# License
[MIT](/LICENSE.md)
