from textnode import TextNode
from htmlnode import HTMLNode
import inline_markdown

def main():
    text = "This is text with a [link](https://www.example.com) and [another](https://www.example.com/another)"
    result = inline_markdown.extract_markdown_links(text)
    print(result)

main()