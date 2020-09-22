# Replacer function
def replace_chunk(content, marker, chunk):
    replacer = re.compile(
        r"<!\-\- {} starts \-\->.*<!\-\- {} ends \-\->".format(marker, marker),
        re.DOTALL,
    )
    chunk = "<!-- {} starts -->\n{}\n<!-- {} ends -->".format(marker, chunk, marker)
    return replacer.sub(chunk, content)

# Open JSON file
root = pathlib.Path(__file__).parent.parent.resolve()
with open( root / "filename.json", 'r') as filehandle:
  object_list = json.load(filehandle)
  
# Convert number to ordinal
def ord(n):
    return str(n)+("th" if 4<=n%100<=20 else {1:"st",2:"nd",3:"rd"}.get(n%10, "th"))

# date time using ordinal
def dtStylish(dt,f):
    return dt.strftime(f).replace("{th}", ord(dt.day))

# pretty printing json
def pprint(string):
    json_formatted_str = json.dumps(string, indent=2)
    print(json_formatted_str)
