import re
import requests

url = 'http://www.columbia.edu/~fdc/sample.html'
data = requests.get(url).text

subheadings = re.findall(r'<h3 id=".*?">(.*?)</h3>', data)

print(subheadings)
