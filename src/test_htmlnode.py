import unittest
from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_props_to_html_with_props(self):
        # Test with some properties
        node = HTMLNode(props={"href": "https://www.google.com", "target": "_blank"})
        self.assertEqual(node.props_to_html(), ' href="https://www.google.com" target="_blank"')
    
    def test_props_to_html_without_props(self):
        # Test with None props
        node = HTMLNode()
        self.assertEqual(node.props_to_html(), "")
    
    def test_props_to_html_empty_props(self):
        # Test with empty props dictionary
        node = HTMLNode(props={})
        self.assertEqual(node.props_to_html(), "")

if __name__ == "__main__":
    unittest.main()