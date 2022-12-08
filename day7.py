with open(file="./input/day7") as file:
    lines = file.read().splitlines()
    
    
part_1 = False

all_paths = {}
sizes = {'/' : { 'size' : 0, 'children' : {}, 'path' : '/' } }
current_dir = sizes['/']
path = '/'
for line in lines:
    if '$ cd' in line:
        dir = line.replace('$ cd ', '')
        if dir == '/': 
            pass
        elif dir == '..':
            path = path[0:path.rfind('/')]
            pathlist = path.split('/')[1:]
            if pathlist == []:
                current_dir = sizes['/']
            else:
                current_dir = sizes['/']['children'][pathlist[0]]
            for subdir in pathlist[1:]:
                current_dir
                current_dir = current_dir['children'][subdir]
        else:
            path += (dir if path == '/' else ('/' + dir))
            current_dir = current_dir['children'][dir]
            current_dir['path'] = path
    elif '$ ls' in line:
        pass
    elif line[0:3] == 'dir':
        dir = line[4:]
        if 'dir' not in current_dir['children']:
            current_dir['children'][dir] = { 'size': 0, 'children' : {} }
    else:
        size = int(line.split(' ')[0])
        #current_dir['size'] += size
        temp = sizes['/']
        temp['size'] += size
        if not part_1:
            all_paths[temp['path']] = temp['size']
        if path != '/':
            for subdir in path.split('/')[1:]:
                temp = temp['children'][subdir]
                temp['size'] += size
                if temp['size'] <= 100_000 or not part_1:
                    all_paths[temp['path']] = temp['size']
                else:
                    all_paths[temp['path']] = 0
                    
if part_1 :
    print(sum(all_paths.values()))
else:
    total_space = 70_000_000
    used_space = all_paths['/']
    available = total_space - used_space
    required = 30_000_000
    to_delete = required - available
    
    smallest_size = total_space
    for path, size in all_paths.items():
        if size > to_delete and size < smallest_size:
            smallest_size = size
            
    print(smallest_size)