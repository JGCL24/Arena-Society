# Re-write README.md as UTF-8 (no BOM) and normalize line endings to LF
p = 'README.md'
with open(p, 'rb') as f:
    raw = f.read()
# Try to decode using utf-8 (replace invalid chars)
text = raw.decode('utf-8', errors='replace')
# Normalize line endings to LF
text = text.replace('\r\n', '\n').replace('\r', '\n')
# Ensure trailing newline
if not text.endswith('\n'):
    text = text + '\n'
# Write back as UTF-8 without BOM
with open(p, 'w', encoding='utf-8', newline='\n') as f:
    f.write(text)
print('Rewrote README.md (utf-8, LF). Length:', len(text))
