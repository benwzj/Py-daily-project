#################################################################
###  nonlocal concept

def test_scopes():
  x = 'spam'
  def change_local():
    x = 'local_spam'
  def change_nonlocal():
    nonlocal x
    x = 'nonlocal_spam'
  def change_global():
    global x
    x = "global_spam"
  
  x = "test_spam"
  change_local()
  print (x)
  change_nonlocal()
  print(x)
  change_global()
  print(x)

test_scopes()
print(x)


