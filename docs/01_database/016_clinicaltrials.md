```

If you just want to get the table, you can try pandas read_html() function:

import pandas as pd

url = "https://clinicaltrials.gov/ct2/archive/NCT03245346"

df = pd.read_html(url)[0]
```

```
url_detail = "https://clinicaltrials.gov/ct2/history/NCT03245346"

df = pd.read_html(url_detail)[0]

```




https://clinicaltrials.gov/ct2/show/study/NCT04966923?term=tp53&recrs=a&draw=2&rank=1