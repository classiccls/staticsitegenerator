from textnode import TextType
from textnode import TextNode
from htmlnode import HTMLNode

def main():
    new_text_node = TextNode("czapla", TextType.BOLD, "morda")
    print(new_text_node)
    new_html_node = HTMLNode("tag", "value", "children", "props")
    print(new_html_node)

main()