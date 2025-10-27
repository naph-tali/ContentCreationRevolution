import chardet

input_file = 'cosmic_revolution_engine_CLEAN.py'
output_file = 'cosmic_revolution_engine_CLEAN_utf8.py'

with open(input_file, 'rb') as f:
    raw_data = f.read()
    result = chardet.detect(raw_data)
    print(f'Original encoding: {result}')
    print(f'BOM detected: {raw_data.startswith(b\"\xef\xbb\xbf\")}')

# Decode and re-encode as UTF-8 without BOM
text = raw_data.decode(result['encoding'])
with open(output_file, 'w', encoding='utf-8') as f:
    f.write(text)

print(f'File saved as UTF-8 without BOM: {output_file}')
