lines_data = []
with open('f5-vip-sample.txt', 'r') as logfile:
    pairs = {}
    for line in logfile:
        new_entry = False
        if line[0].isspace():
          fields = line.strip().split(':')
        else:
          double_colon_idx = line.find('::')
          line = line[double_colon_idx+2:]
          new_entry = True
        fields = line.strip().split(':')
        if new_entry and pairs:
          lines_data.append(pairs)
          pairs = {}
        if len(fields) >= 2:
          key = fields[0]
          value = fields[1]
          pairs[key.strip()] = value.strip()
    lines_data.append(pairs)
headers = lines_data[0].keys()
header_str = ','.join(headers)
with open('report.csv','w') as out:
  out.write(header_str + '\n')
  for entry in lines_data:
    _line = []
    for key in headers:
      _line.append(entry[key])
    out.write(','.join(_line) + '\n')