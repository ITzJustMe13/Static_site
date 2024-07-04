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

def split_nodes_image(old_nodes):
    new_nodes = []
    for node in old_nodes:
        image_tups = extract_markdown_images(node.text)
        remaining_text = node.text

        for image_tup in image_tups:
            parts = remaining_text.split(f"![{image_tup[0]}]({image_tup[1]})", 1)

            if parts[0]:
                new_nodes.append(TextNode(parts[0], node.text_type))

            new_nodes.append(TextNode(image_tup[0],text_type_image,image_tup[1]))

            remaining_text = parts[1]
        
        if remaining_text:
            new_nodes.append(TextNode(remaining_text, node.text_type))
    
    return new_nodes

def split_nodes_link(old_nodes):
    new_nodes = []
    for node in old_nodes:
        link_tups = extract_markdown_links(node.text)
        remaining_text = node.text

        for link_tup in link_tups:
            parts = remaining_text.split(f"[{link_tup[0]}]({link_tup[1]})", 1)

            if parts[0]:
                new_nodes.append(TextNode(parts[0], node.text_type))

            new_nodes.append(TextNode(link_tup[0],text_type_link,link_tup[1]))

            remaining_text = parts[1]
        
        if remaining_text:
            new_nodes.append(TextNode(remaining_text, node.text_type))
    
    return new_nodes