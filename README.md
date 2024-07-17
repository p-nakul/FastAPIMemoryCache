# FastAPIMemoryCache
Simple memory cache to store key value pairs which is accesible over fastapi 

Simple Memory cache implementation using sqllite to store key-value (**str-json**) pairs 
in memory for faster accessibility over RestAPI

##### Rest endpoints
1. set *sets a key value pair*
2. get *gets value using key*

#### TODO
```
- [] Get method return msg when key doesnot exists
- [] Set method overwrite key 
- [] Add TTL field in db
- [] Expire data when they are read
- [] Expire data randomly in background 

```