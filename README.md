# getpass2
A better lib compared with standard 'getpass' in Python, easier and simpler to use.

---

## How to install:


```
pip install getpass2
```

## How to use:

Make sure you are in your console.

```Python
from getpass2 import getpass
```

And then the function `getpass` will return what you typed and show how many characters you have typed!

## example

When the mode is 'n' means show numbers. You can see it as follows:

```Python
#coding:utf-8
import sys

from getpass2 import *

if __name__ == '__main__':
	print getpass(prompt='\bplease input your username(there should contains no space):', mode='n')
	
```

![can delete chars and show current typed numbers of chars](https://github.com/guoruibiao/getpass2/raw/master/images/getpass2-1.0.2_candel.gif)



```Python
#coding:utf-8
import sys

from getpass2 import *

if __name__ == '__main__':
    print getpass(prompt='\bplease input your username(there should contains no space):', mode='r', delimiter='*')
```

![can delete chars and show replaced by customed delimiter](https://github.com/guoruibiao/getpass2/raw/master/images/getpass2-1.0.2_candel_replace.gif)

If something doesn't work, you can also copy the source named getpass2.py to your workspace. That will be OK!

## Tips

You can custom your tip statement for the prompt parameter.

And most importantly, when you want to custom you tip parameter, remember to add a '%d' in it. That's really really important.

Finally, hope you can get happiness after using getpass2. Thank you!
