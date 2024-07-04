import re
from textnode import (
    TextNode,
    text_type_text,
    text_type_bold,
    text_type_italic,
    text_type_code,
)

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != text_type_text:
            new_nodes.append(node)
        else:
            segments = node.text.split(delimiter)
            if len(segment) % 2 == 0:
                raise ValueError(f"Unmatched delimiter '{delimiter}' found in text: {node.text}")
                
            for i , segment in enumerate(segments):
                if i % 2 == 0:
                    new_nodes.append(TextNode(segment,text_type_text))
                else:
                    new_nodes.append(TextNode(segment,new_text_type))
    return new_nodes

def extract_markdown_images(text):
    matches = re.findall(r"!\[(.*?)\]\((.*?)\)",text)
    return matches

def extract_markdown_links(text):
    matches = re.findall(r"\[(.*?)\]\((.*?)\)",text)
    return matches