import tagui as t

'''
search in the F12, to locate the element: //input[@name="q"] or //input[@class="gLFyf gsfi"]
for multiple selection: t.read(//div[@class="r"])[0]/a/@href')

select by content: //h2[contains(.,"Selector")]

select by id:  //*[@id="abc"]

t.present() to check whether some element exist or not

chrome plugin: xpath helper

https://devhints.io/xpath

'''


#--------------demo 1 -----------------------------
'''
t.init()
t.url('https://google.com')
print("test_tagui ok!")

t.type('//input[@name="q"]', 'weather[enter]')


t.type('//input[@name="q"]', '[clear]')

temp = t.read('//span[@id="wob_pp"]')
'''


#------------demo 2 --------------------------------
t.url('https://www.goodreads.com/list/show/17347.Books_that_ll_help_you_deliver_stunning_presentations')



print(temp)

pass
