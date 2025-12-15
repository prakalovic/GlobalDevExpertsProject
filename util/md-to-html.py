#!/usr/bin/env python3
"""
Convert markdown files to HTML with Mermaid diagram support
Usage: python md-to-html.py <input.md> [output.html]
"""

import sys
import re
import subprocess
import tempfile
import base64
from pathlib import Path

def convert_mermaid_to_image(mermaid_content):
    """Convert Mermaid content to base64 encoded image using mermaid-cli"""
    import platform
    import os
    
    try:
        # Create temporary files
        with tempfile.NamedTemporaryFile(mode='w', suffix='.mmd', delete=False, encoding='utf-8') as mmd_file:
            mmd_file.write(mermaid_content)
            mmd_path = mmd_file.name
        
        with tempfile.NamedTemporaryFile(suffix='.png', delete=False) as png_file:
            png_path = png_file.name
        
        try:
            # Try different command variants for cross-platform compatibility
            commands_to_try = []
            
            if platform.system() == 'Windows':
                commands_to_try = [
                    ['npx.cmd', '@mermaid-js/mermaid-cli', '-i', mmd_path, '-o', png_path, '-t', 'default', '-b', 'white', '--scale', '5', '--width', '1800', '--height', '1200', '--configFile', 'null'],
                    ['npx', '@mermaid-js/mermaid-cli', '-i', mmd_path, '-o', png_path, '-t', 'default', '-b', 'white', '--scale', '5', '--width', '1800', '--height', '1200'],
                    ['mmdc.cmd', '-i', mmd_path, '-o', png_path, '-t', 'default', '-b', 'white', '--scale', '5', '--width', '1800', '--height', '1200'],
                    ['mmdc', '-i', mmd_path, '-o', png_path, '-t', 'default', '-b', 'white', '--scale', '5', '--width', '1800', '--height', '1200']
                ]
            else:
                commands_to_try = [
                    ['npx', '@mermaid-js/mermaid-cli', '-i', mmd_path, '-o', png_path, '-t', 'default', '-b', 'white', '--scale', '5', '--width', '1800', '--height', '1200'],
                    ['mmdc', '-i', mmd_path, '-o', png_path, '-t', 'default', '-b', 'white', '--scale', '5', '--width', '1800', '--height', '1200']
                ]
            
            success = False
            for cmd in commands_to_try:
                try:
                    result = subprocess.run(cmd, check=True, capture_output=True, text=True, timeout=30)
                    success = True
                    break
                except (subprocess.CalledProcessError, FileNotFoundError, subprocess.TimeoutExpired):
                    continue
            
            if not success:
                raise Exception("Mermaid CLI not found or failed")
            
            # Verify output file exists
            if not os.path.exists(png_path) or os.path.getsize(png_path) == 0:
                raise Exception("PNG output file not created")
            
            # Read and encode the image
            with open(png_path, 'rb') as img_file:
                img_data = img_file.read()
                img_base64 = base64.b64encode(img_data).decode('utf-8')
            
            return f'<div class="mermaid-container"><img src="data:image/png;base64,{img_base64}" alt="Mermaid Diagram" style="max-width: 100%; height: auto; margin: 20px auto; display: block; border: 1px solid #e0e0e0; border-radius: 8px; box-shadow: 0 2px 8px rgba(0,0,0,0.1); background: white; padding: 20px;" onclick="this.style.maxWidth = this.style.maxWidth === \'100%\' ? \'none\' : \'100%\'; this.style.cursor = this.style.cursor === \'zoom-out\' ? \'zoom-in\' : \'zoom-out\';" title="Click to zoom"></div>'
            
        finally:
            # Clean up temporary files
            try:
                if os.path.exists(mmd_path):
                    os.unlink(mmd_path)
                if os.path.exists(png_path):
                    os.unlink(png_path)
            except:
                pass
            
    except Exception as e:
        # Fallback to HTML/CSS version
        print(f"Warning: Could not convert Mermaid to image: {e}")
        print("To enable image conversion, install: npm install -g @mermaid-js/mermaid-cli")
        print("Falling back to HTML/CSS version")
        return convert_mermaid_to_html_fallback(mermaid_content)

def convert_tables_to_html(text):
    """Convert markdown tables to HTML tables"""
    lines = text.split('\n')
    result_lines = []
    i = 0
    
    while i < len(lines):
        line = lines[i]
        
        # Check if this line looks like a table header
        if '|' in line and i + 1 < len(lines) and '|' in lines[i + 1] and ('---' in lines[i + 1] or ':--' in lines[i + 1]):
            # Found a table, process it
            table_lines = []
            
            # Get header
            header_cells = [cell.strip() for cell in line.split('|') if cell.strip()]
            table_lines.append('<table>')
            table_lines.append('<thead>')
            table_lines.append('<tr>')
            for cell in header_cells:
                table_lines.append(f'<th>{cell}</th>')
            table_lines.append('</tr>')
            table_lines.append('</thead>')
            
            # Skip separator line
            i += 2
            
            # Process data rows
            table_lines.append('<tbody>')
            while i < len(lines) and '|' in lines[i]:
                data_cells = [cell.strip() for cell in lines[i].split('|') if cell.strip() or lines[i].split('|').index(cell) > 0]
                if data_cells:  # Only process non-empty rows
                    table_lines.append('<tr>')
                    for cell in data_cells:
                        table_lines.append(f'<td>{cell}</td>')
                    table_lines.append('</tr>')
                i += 1
            
            table_lines.append('</tbody>')
            table_lines.append('</table>')
            
            result_lines.extend(table_lines)
            i -= 1  # Adjust because we'll increment at end of loop
        else:
            result_lines.append(line)
        
        i += 1
    
    return '\n'.join(result_lines)

def convert_mermaid_to_html_fallback(mermaid_content):
    """Fallback HTML/CSS version when mermaid CLI is not available"""
    html = '<div class="flowchart">\n'
    
    # Parse the basic structure and check current status
    if 'Development Phase' in mermaid_content and 'Translation Phase' in mermaid_content:
        # Check what status the Mermaid shows
        dev_status = "Dev Workflow ✓" if "Dev Workflow" in mermaid_content else "TBD"
        trans_status = "Regression ✓" if "Testing: Regression" in mermaid_content else "TBD"
        code_status = "Final Regression ✓" if "Final Regression" in mermaid_content else "Regression ✓"
        
        dev_class = "decided" if "✓" in dev_status else "pending"
        trans_class = "decided" if "✓" in trans_status else "pending"
        code_class = "decided"
        
        html += f'''
  <div class="flow-container">
    <div class="phase-column">
      <div class="box neutral">Development Phase</div>
      <div class="vertical-arrow">↓</div>
      <div class="box {dev_class}">Testing: {dev_status}</div>
      <div class="dotted-line">⋯</div>
      <div class="box future">Tools & Methods<br/>TBD</div>
    </div>
    
    <div class="horizontal-arrow">→</div>
    
    <div class="phase-column">
      <div class="box neutral">Translation Phase</div>
      <div class="vertical-arrow">↓</div>
      <div class="box {trans_class}">Testing: {trans_status}</div>
      <div class="dotted-line">⋯</div>
      <div class="box future">Tools & Methods<br/>TBD</div>
    </div>
    
    <div class="horizontal-arrow">→</div>
    
    <div class="phase-column">
      <div class="box neutral">Code Freeze Phase</div>
      <div class="vertical-arrow">↓</div>
      <div class="box {code_class}">Testing: {code_status}</div>
      <div class="dotted-line">⋯</div>
      <div class="box future">Tools & Methods<br/>TBD</div>
    </div>
    
    <div class="horizontal-arrow">→</div>
    
    <div class="phase-column">
      <div class="box neutral">Release</div>
    </div>
  </div>
'''
    
    html += '</div>\n'
    return html

def convert_md_to_html(md_content):
    """Convert markdown content to HTML"""
    # Split content into blocks to handle mermaid separately
    blocks = []
    current_block = []
    in_mermaid = False
    
    for line in md_content.split('\n'):
        if line.strip() == '```mermaid':
            if current_block:
                blocks.append(('text', '\n'.join(current_block)))
                current_block = []
            in_mermaid = True
            mermaid_lines = []
        elif line.strip() == '```' and in_mermaid:
            blocks.append(('mermaid', '\n'.join(mermaid_lines)))
            in_mermaid = False
        elif in_mermaid:
            mermaid_lines.append(line)
        else:
            current_block.append(line)
    
    if current_block:
        blocks.append(('text', '\n'.join(current_block)))
    
    # Process each block
    html_blocks = []
    for block_type, content in blocks:
        if block_type == 'mermaid':
            html_blocks.append(convert_mermaid_to_image(content))
        else:
            # Process text content
            html = content
            
            # Convert markdown tables to HTML tables
            html = convert_tables_to_html(html)
            
            # Headers
            html = re.sub(r'^# (.*)$', r'<h1>\1</h1>', html, flags=re.MULTILINE)
            html = re.sub(r'^## (.*)$', r'<h2>\1</h2>', html, flags=re.MULTILINE)
            html = re.sub(r'^### (.*)$', r'<h3>\1</h3>', html, flags=re.MULTILINE)
            html = re.sub(r'^#### (.*)$', r'<h4>\1</h4>', html, flags=re.MULTILINE)
            html = re.sub(r'^##### (.*)$', r'<h5>\1</h5>', html, flags=re.MULTILINE)
            
            # Bold and italic
            html = re.sub(r'\*\*(.*?)\*\*', r'<strong>\1</strong>', html)
            html = re.sub(r'\*(.*?)\*', r'<em>\1</em>', html)
            
            # Code blocks and inline code
            html = re.sub(r'```(\w+)?\n(.*?)\n```', r'<pre><code>\2</code></pre>', html, flags=re.DOTALL)
            html = re.sub(r'`([^`]+)`', r'<code>\1</code>', html)
            
            # Lists
            html = re.sub(r'^- (.*)$', r'<li>\1</li>', html, flags=re.MULTILINE)
            html = re.sub(r'^\d+\. (.*)$', r'<li>\1</li>', html, flags=re.MULTILINE)
            
            # Checkboxes
            html = re.sub(r'- \[ \] (.*)', r'<li>☐ \1</li>', html)
            html = re.sub(r'- \[x\] (.*)', r'<li>☑ \1</li>', html)
            
            # Wrap consecutive list items in ul tags
            html = re.sub(r'(<li>.*?</li>)(\s*<li>.*?</li>)*', r'<ul>\g<0></ul>', html, flags=re.DOTALL)
            
            # Convert double newlines to paragraph breaks
            html = re.sub(r'\n\s*\n', '\n</p>\n<p>\n', html)
            
            # Wrap in paragraph tags if not already wrapped
            if not html.strip().startswith('<'):
                html = f'<p>\n{html}\n</p>'
            
            html_blocks.append(html)
    
    return '\n'.join(html_blocks)

def process_mermaid(content):
    """Convert Mermaid blocks to HTML with Mermaid.js"""
    def replace_mermaid(match):
        mermaid_code = match.group(1)
        return f'<div class="mermaid">\n{mermaid_code}\n</div>'
    
    return re.sub(r'```mermaid\n(.*?)\n```', replace_mermaid, content, flags=re.DOTALL)

def main():
    if len(sys.argv) < 2:
        print("Usage: python md-to-html.py <input.md> [output.html]")
        sys.exit(1)
    
    input_file = Path(sys.argv[1])
    output_file = Path(sys.argv[2]) if len(sys.argv) > 2 else input_file.with_suffix('.html')
    
    if not input_file.exists():
        print(f"Error: {input_file} not found")
        sys.exit(1)
    
    # Read markdown content
    with open(input_file, 'r', encoding='utf-8') as f:
        md_content = f.read()
    
    # Convert markdown to HTML (handles mermaid blocks separately)
    html_body = convert_md_to_html(md_content)
    
    # Create full HTML document
    full_html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{input_file.stem}</title>
    <style>
        body {{ font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; max-width: 800px; margin: 0 auto; padding: 20px; line-height: 1.6; }}
        h1, h2, h3, h4 {{ color: #333; }}
        code {{ background: #f4f4f4; padding: 2px 4px; border-radius: 3px; }}
        pre {{ background: #f4f4f4; padding: 10px; border-radius: 5px; overflow-x: auto; }}
        ul, ol {{ padding-left: 20px; }}
        li {{ margin: 5px 0; }}
        
        table {{ 
            border-collapse: collapse; 
            width: 100%; 
            margin: 20px 0; 
            font-size: 14px;
        }}
        th, td {{ 
            border: 1px solid #ddd; 
            padding: 8px 12px; 
            text-align: left; 
            vertical-align: top;
        }}
        th {{ 
            background-color: #f2f2f2; 
            font-weight: 600;
            position: sticky;
            top: 0;
        }}
        tr:nth-child(even) {{ 
            background-color: #f9f9f9; 
        }}
        tr:hover {{ 
            background-color: #f5f5f5; 
        }}
        
        .flowchart {{
            margin: 20px 0;
            display: flex;
            justify-content: center;
        }}
        
        .mermaid-container {{
            text-align: center;
            margin: 30px 0;
        }}
        
        .mermaid-container img {{
            cursor: zoom-in;
            transition: all 0.3s ease;
        }}
        
        .mermaid-container img:hover {{
            box-shadow: 0 4px 16px rgba(0,0,0,0.2) !important;
        }}
        
        .flow-container {{
            display: flex;
            align-items: flex-start;
            gap: 20px;
        }}
        
        .phase-column {{
            display: flex;
            flex-direction: column;
            align-items: center;
            gap: 10px;
        }}
        
        .box {{
            padding: 8px 16px;
            border-radius: 8px;
            border: 2px solid;
            font-weight: 500;
            min-width: 120px;
            text-align: center;
            font-size: 14px;
            min-height: 40px;
            display: flex;
            align-items: center;
            justify-content: center;
        }}
        
        .box.decided {{
            background-color: #2d5a2d;
            border-color: #4caf50;
            color: #ffffff;
        }}
        
        .box.pending {{
            background-color: #5a2d2d;
            border-color: #f44336;
            color: #ffffff;
        }}
        
        .box.future {{
            background-color: #5a4d2d;
            border-color: #ff9800;
            color: #ffffff;
        }}
        
        .box.neutral {{
            background-color: #404040;
            border-color: #666666;
            color: #ffffff;
        }}
        
        .horizontal-arrow {{
            font-size: 24px;
            color: #666;
            font-weight: bold;
            align-self: flex-start;
            margin-top: 25px;
        }}
        
        .vertical-arrow {{
            font-size: 18px;
            color: #666;
            font-weight: bold;
        }}
        
        .dotted-line {{
            font-size: 18px;
            color: #999;
            font-weight: bold;
        }}
    </style>
</head>
<body>
{html_body}
</body>
</html>"""
    
    # Write HTML file
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(full_html)
    
    print(f"Converted {input_file} to {output_file}")

if __name__ == "__main__":
    main()