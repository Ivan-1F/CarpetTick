import re

patterns = [
    re.compile(r'Avg\. server tick time: \d\.?\d*ms'),  # Avg. server tick time: 0.991ms
    re.compile(r'Average tick time: \d\.?\d*ms'),  # Average tick time: 0.359ms
    re.compile(r'overworld:'),  # overworld:
    re.compile(r'the_nether:'),  # the_nether:
    re.compile(r'the_end:'),  # the_end:
    re.compile(r'Top 10 counts:'),  # Top 10 counts:
    re.compile(r'Top 10 CPU hogs:'),  # Top 10 CPU hogs:
    re.compile(r' - .*: \d\.?\d*ms'),  # - Spawning and Random Ticks: 0.060ms
    re.compile(r'The Rest, whatever that might be: \d\.?\d*ms')  # - The Rest, whatever that might be: 0.905ms
]


def accept(text: str):
    for pattern in patterns:
        if re.match(pattern, text):
            return True
    return False
