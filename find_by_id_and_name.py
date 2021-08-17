from selenium import webdriver
d = webdriver.Chrome()
d.get("./test01.html")
id="nav"
find_element_by_id(id)
name="Trick"
find_element_by_name(name)

class_name = "dom_test"
find_element_by_class_name(class_name)
tag_name = "p"
find_element_by_tag_name(tag_name)
