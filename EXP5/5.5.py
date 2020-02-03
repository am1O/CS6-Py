  string = "the is the main string"
  sub = "string"
  try:
    print(string.index(sub))
  except Exception as e:
    print("Not found")
