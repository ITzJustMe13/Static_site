class HTMLNode:

    def __init__(self,tag=None,value=None,children=None,props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError("to_html method not implemented")

    def props_to_html(self):
        final_string = ""
        if self.props:
            for key in self.props:
                string = f' {key}="{self.props[key]}"'
                final_string += string
        return final_string

    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, children: {self.children}, {self.props})"

class LeafNode(HTMLNode):

    def __init__(self,tag,value,props=None):
        super().__init__(tag,value,None,props)
        

    def to_html(self):
        if self.value is None:
            raise ValueError("No value")
        if self.tag is None:
            return self.value
        
        html_str = f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"

        return html_str
    
    def __repr__(self):
        return f"LeafNode({self.tag}, {self.value}, {self.props})"
    

class ParentNode(HTMLNode):

    def __init__(self,tag,children,props=None):
        super().__init__(tag,None,children,props)
        

    def to_html(self):
        if self.tag is None:
            raise ValueError("NO TAG PROVIDED")
        if self.children is None:
            raise ValueError("NO CHILDREN PROVIDED")
        final_string = ""
        final_string += f"<{self.tag}>"
        for child in self.children:
            if hasattr(child,'to_html'):
                final_string += child.to_html()
            else:
                raise TypeError("Child node does not have a 'to_html' method")
        final_string += f"</{self.tag}>"
        return final_string
    
    def __repr__(self):
        return f"ParentNode({self.tag}, children: {self.children}, {self.props})"