import streamlit.components.v1 as components

def markmap(data, height=600):
    data = str(data)
    markdown_style = '''
            <style>
                svg {{
                    width: 100%;
                    height: {}px;
                }}
            </style>'''.format(height)
    markdown_html = f'''
        {markdown_style}
        <script src="https://cdn.jsdelivr.net/npm/markmap-autoloader"></script>
            
        <div class='markmap'>{data}</div>
    '''

    markmap_component = components.html(markdown_html, height=height)
    return markmap_component
