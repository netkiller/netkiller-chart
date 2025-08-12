from netkiller.markdown import Markdown
from netkiller.mindmap import Mindmap

data = """
# 操作系统
- Operating System
  - Linux
    - Redhat
    - CentOS
    - Rocky Linux
  - Apple OS  
    - macOS
      - nojava
      - catalina
    - iPadSO
    - tvOS 
    - iOS
    - watchOS 
  - Unix
    - Solaris
    - Aix
    - Hp-Ux
    - Sco Unix
"""

markdown = Markdown(data)
jsonData = markdown.mindmap()

mindmap = Mindmap(jsonData)
mindmap.save('example.svg')
