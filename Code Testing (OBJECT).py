import re
import sys


exitCmd = re.compile('(?:Exit|Quit|Close|End|Suicide)', flags=re.IGNORECASE)
examineCmd = re.compile('(?:Look at|Examine|Inspect) (\w+)', flags=re.IGNORECASE)
inventoryCmd = re.compile('(?:Inventory|Items)', flags=re.IGNORECASE)
helpCmd = re.compile('(?:Help|H|\?|-H|-Help)(.*)', flags=re.IGNORECASE)

print(input())