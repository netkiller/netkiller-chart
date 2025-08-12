import xmind

workbook = xmind.load("my_map.xmind")
sheet = workbook.getPrimarySheet()
sheet.setTitle("我的思维导图")
root = sheet.getRootTopic()
root.setTitle("主题A")

sub1 = root.addSubTopic()
sub1.setTitle("子节点1")

sub2 = root.addSubTopic()
sub2.setTitle("子节点2")

# 给子节点2添加子节点21
sub21 = sub2.addSubTopic()
sub21.setTitle("子节点21")

xmind.save(workbook, path="/tmp/my_map.xmind")
