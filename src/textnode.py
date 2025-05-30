from enum import Enum

from htmlnode import LeafNode

class TextType(Enum):
    TEXT = "text"
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code"
    LINK = "link"
    IMAGE = "image"

class TextNode():
    def __init__(self, text, text_type, url = None):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, other):
        if not isinstance(other, TextNode):
            return False
        return self.text == other.text and self.text_type == other.text_type and self.url == other.url
    
    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type.value}, {self.url})"
    
def text_node_to_html_node(text_node):
    if text_node.text_type.value == "text":
        return LeafNode(None, text_node.text)
    elif text_node.text_type.value == "bold":
        return LeafNode("b", text_node.text)
    elif text_node.text_type.value == "italic":
        return LeafNode("i", text_node.text)
    elif text_node.text_type.value == "code":
        return LeafNode("code", text_node.text)
    elif text_node.text_type.value == "link":
        if text_node.url is None:
            raise Exception("No url provided")
        return LeafNode("a", text_node.text, {"href": text_node.url})
    elif text_node.text_type.value == "image":
        if text_node.url is None:
            raise Exception("No url provided")
        return LeafNode("img", "", {"src": text_node.url, "alt": text_node.text})
    else:
        raise Exception("Invalid node type")