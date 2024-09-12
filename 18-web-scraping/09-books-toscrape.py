from bs4 import BeautifulSoup

html_content = """<html>
    <body>
        <p>Hello, World!</p>
        <a href="example.com">Link 1 : example.com</a>
        <a href="example.com">Link 2 : example.com</a>
        <div>
            <div class="my-class">
                 <p>This is my class.</p>
            </div>
        </div>
    </body></html>
"""
soup = BeautifulSoup(html_content, 'html.parser')

print("======================================================")
print("Searching and Navigating the Tree:")
# Find the first <p> tag
first_paragraph = soup.find('p')
print(first_paragraph.text)
print("------------------------------------")

# # Find all <a> tags with 'href' containing 'example.com'
links = soup.find_all('a', href='example.com')
for link in links:
    print(link.text)
print("------------------------------------")

# Select all elements with class 'my-class' inside a <div>
selected_elements = soup.select('div .my-class')
print(selected_elements)
for element in selected_elements:
    print(element)
    print(element.p)
    print(element.p.text)
print("------------------------------------")

print("Accessing Tag Attributes:")
tag = soup.find('a')
print(tag.name)  # Outputs: 'a'

link = soup.find('a')
href_value = link.get('href')
print(href_value)
print("======================================================")
print("Navigating the Tree:")
parent_tag = tag.parent
all_parents = list(tag.parents)
for parent in all_parents:
    print(parent)
    print("------------------------------------")

print("======================================================")
print("Modifying the Document:")
tag = soup.find('p')

print(tag)
tag.string = "New content"
print(tag)

print("======================================================")
print("Output Formatting:")
pretty_html = soup.prettify()
print(pretty_html)
