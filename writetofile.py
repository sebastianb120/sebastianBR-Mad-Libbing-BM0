def opentext():
  with open("demofile.txt", "r") as f:
    content = f.read()
    text_area.delete("1.0", END)
    text_area.insert("1.0",content)


def savetext():
  text = text_area.get("1.0", END)
  with open('demofile.txt', 'w') as f:
    f.write(text)