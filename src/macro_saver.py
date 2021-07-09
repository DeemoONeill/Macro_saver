# %%
from bs4 import BeautifulSoup
from selenium import webdriver
import json
# %%

driver = webdriver.Firefox()
driver.get("https://roll20.net/")
# %%
input("log in navigate to your game and then press enter here")
driver.find_element_by_css_selector("#ui-id-5").click()
macros = driver.find_elements_by_css_selector("td.name")
macro_names = [macro.text[1:] for macro in macros[:-2]]
# %%
macro_bodies = []
for macro in macros:
    macro.click()
    macro_text = driver.find_elements_by_css_selector("textarea.macro")
    macro_bodies.append("".join([name.text for name in macro_text]).strip())
    buttons = driver.find_elements_by_tag_name("button")
    for button in buttons:
        if button.text == "Cancel":
            button.click()
            break
macros = dict(zip(macro_names, macro_bodies))
print(macros)
# %%
with open("macros.json", "w") as f:
    json.dump(macros,f, indent=0)