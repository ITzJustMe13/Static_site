block_type_paragraph = "paragraph"
block_type_heading = "heading"
block_type_code = "code"
block_type_quote = "quote"
block_type_unordered_list = "unordered_list"
block_type_ordered_list = "ordered_list"


def markdown_to_blocks(markdown):
    blocks = markdown.split("\n\n")
    new_blocks = []
    for block in blocks:
        stripped_block = block.strip()
        if stripped_block:
            new_blocks.append(stripped_block)
    return new_blocks

def block_to_block_type(block):
    new_block = block.split("\n")

    if new_block[0].startswith("```") and new_block[-1].startswith("```"):
        return block_type_code
    elif new_block[0].startswith("#"):
        heading_count = 0
        while heading_count < len(new_block[0]) and new_block[0][heading_count] == "#":
            heading_count += 1
        if 1 <= heading_count <= 6 and new_block[0][heading_count] == " ":
            return block_type_heading
    elif all(block.startswith("> ") for block in new_block):
        return block_type_quote
    elif all(block.startswith("* ") for block in new_block) or all(block.startswith("- ") for block in new_block):
        return block_type_unordered_list
    elif all(block.startswith(f"{i + 1}. ") for i,block in enumerate(new_block)):
        return block_type_ordered_list
    else:
        return block_type_paragraph

