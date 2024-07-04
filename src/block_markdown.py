def markdown_to_blocks(markdown):
    blocks = markdown.split("\n\n")
    new_blocks = []
    for block in blocks:
        stripped_block = block.strip()
        if stripped_block:
            new_blocks.append(stripped_block)
    return new_blocks
