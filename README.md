# docekr_retag
docekr retag image without by pull and push
# Usage
```python
from docker_retag import Registry
registyr_ins = Registry("username", "password", "registry_url", "new_tag", "old_tag")

registyr_ins.add_new_tag_by_registry()
```
