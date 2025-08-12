from netkiller.markdown import Markdown

from src.netkiller.mindmap import Mindmap


def main():
    data = """# Netkiller Linux 手札
- Linux
  - Redhat
  - CentOS
  - Rocky Linux
  - AlmaLinux
    """

    markdown = Markdown(data)
    jsonData = markdown.mindmap()

    mindmap = Mindmap(jsonData)
    mindmap.xmind('none.xmind', 'test.xmind')


if __name__ == "__main__":
    main()
