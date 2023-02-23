
class Language:
  def __init__(self, lang) -> None:
    self.lang = lang
  me = 'Language Class'
  def message(self):
    print("this is "+self.lang+", nice to meet you " + self.me)
  def action(self):
    print("let's action! " + self.lang)

languages = [Language("python"), Language("javascript")]

for language in languages:
  language.message()


