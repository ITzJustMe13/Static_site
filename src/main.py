from textnode import TextNode
from htmlnode import HTMLNode

def main():
    dummy = TextNode("This is a text node", "bold","https://www.boot.dev")
    node = HTMLNode(tag="a", value="Click here", props={"href": "https://www.google.com", "target": "_blank"})
    print(node)
    print(node.props_to_html())
    

main()