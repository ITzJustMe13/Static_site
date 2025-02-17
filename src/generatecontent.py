import os
from pathlib import Path
from block_markdown import markdown_to_html_node


def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    
    if not os.path.exists(dest_dir_path):
        print(f"Creating root directory: {dest_dir_path}")
        os.makedirs(dest_dir_path, exist_ok=True)

    for filename in os.listdir(dir_path_content):
        from_path = os.path.join(dir_path_content, filename)
        dest_path = os.path.join(dest_dir_path, filename)
        
        print(f"Processing: {from_path} -> {dest_path}")

        if os.path.isfile(from_path) and filename.endswith(".md"):
            dest_path = Path(dest_path).with_suffix(".html")
            print(f"Generating file: {from_path} -> {dest_path}")
            generate_page(from_path, template_path, dest_path)
        elif os.path.isdir(from_path):
            print(f"Ensuring sub-directory exists: {dest_path}")
            if not os.path.exists(dest_path):
                os.makedirs(dest_path, exist_ok=True)
            # Recurse into the subdirectory
            generate_pages_recursive(from_path, template_path, dest_path)

def generate_page(from_path, template_path, dest_path):
    print(f" * {from_path} {template_path} -> {dest_path}")
    from_file = open(from_path, "r")
    markdown_content = from_file.read()
    from_file.close()

    template_file = open(template_path, "r")
    template = template_file.read()
    template_file.close()

    node = markdown_to_html_node(markdown_content)
    html = node.to_html()

    title = extract_title(markdown_content)
    template = template.replace("{{ Title }}", title)
    template = template.replace("{{ Content }}", html)

    dest_dir_path = os.path.dirname(dest_path)
    if dest_dir_path != "":
        os.makedirs(dest_dir_path, exist_ok=True)
    to_file = open(dest_path, "w")
    to_file.write(template)


def extract_title(md):
    lines = md.split("\n")
    for line in lines:
        if line.startswith("# "):
            return line[2:]
    raise ValueError("No title found")