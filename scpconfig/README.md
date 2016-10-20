#SCP Configiguration to network gears that can be appened to the config
under a folder create the config to append with filename as the hostname
Run the python script to push the config with the same destination name to all the gears listed in directory
```
yaseen:config myaseen$ ls -ltr
total 16
-rw-r--r--  1 yaseen  101  31 Oct 20 10:19 sw-a.test.com
-rw-r--r--  1 yaseen  101  28 Oct 20 10:19 sw-b.test.com
yaseen:config yaseen$ cat sw-a.test.com
interface vlan 100
no shutdown
yaseen:config yaseen$ cat sw-b.test.com
interface vlan 200
shutdown
```
