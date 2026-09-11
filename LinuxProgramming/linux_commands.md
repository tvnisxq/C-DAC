# Hardware information commands
```bash
● dmesg  # Shows system boot information

● nproc  # Shows CPU details

● lsmod # Shows the status of Modules in the kernel

● free # Shows Memory details
    
    free -h # Shows human readable output
    free -t # Show total for RAM + swap
    free --giga # Shows output in gigabytes
    
● uname # displays Operating System details

    uname -a # displays all information of the OS like kernel, nodename, machine, etc
    uname -s # displays just the kernel name
    uname -i # prints the hardware platform

● hwinfo # Prints hardware details

● hostnamectl # Control the system hostname
```



# Searching commands
Search for PATTERNS in each FILE. Example:
```bash
grep -i 'hello world' menu.sh main.c
```
Patterns may contain multiple patterns separated by newlines 

```bash
● grep [OPTION]... PATTERNS [FILE]... 
    grep -r PATTERN DIR # search recursively for pattern in current directory and its subdirectories 
    grep -i "Ubuntu" file.txt # case insensitive search
    grep -n "gnupg" config.ini # show line numbers
    grep -v "href" index.html # Invert the search: show lines that do not contain 'href'(Inverting the match) 

```


Locate Finds paths containing a specific name; E.g., file.txt.

```bash
● locate [OPTIONS]... PATTERN...
```

```bash
    locate file.txt # finds paths containing file.txt
    locate "*.py" # finds python files known to locate DataBase 
    locate -i "readme" # finds paths of files case-insensitive
    locate -c "*.py" # Instead of listing all the paths, it shows the count of instances
    locate -l 10 "*.py" # Show atleast 10 instances
```

```bash
find . -name "*.py"

```
# File commands


# Compression commands

# Copy commands

# User and group mgmt commands

# Package commands




# Process commands

# System management commands

# Disk usage commands

# Permission commands

# Network commands

# General commands

# Keyboard shortcuts