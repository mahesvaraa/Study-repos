# Count IP Addresses

https://www.codewars.com/kata/526989a41034285187000de4

Implement a function that receives two IPv4 addresses, and returns the number of addresses between them (including the
first one, excluding the last one).

All inputs will be valid IPv4 addresses in the form of strings. The last address will always be greater than the first
one.

**Examples**

```python
*With
input
"10.0.0.0", "10.0.0.50" = > return 50
*With
input
"10.0.0.0", "10.0.1.0" = > return 256
*With
input
"20.0.0.10", "20.0.1.0" = > return 246
```

# Solution

```python
def ips_between(start, end):
    ip_address = int(''.join([bin(int(i))[2:].rjust(8, '0') for i in start.split('.')]), 2)
    ip_address2 = int(''.join([bin(int(i))[2:].rjust(8, '0') for i in end.split('.')]), 2)
    return ip_address2 - ip_address
```